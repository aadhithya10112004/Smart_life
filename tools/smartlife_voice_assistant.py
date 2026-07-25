import os
import io
import tempfile
import streamlit as st
from gtts import gTTS

try:
    import torch  # noqa: F401
except Exception:
    torch = None

try:
    import librosa
    import numpy as np
    import soundfile as sf
except Exception:
    librosa = None
    np = None
    sf = None

DEVICE = "cpu"
SAMPLE_RATE = 16000


def _load_transformers():
    from transformers import AutoModelForSpeechSeq2Seq
    from transformers.models.whisper.processing_whisper import WhisperProcessor
    from transformers.models.blenderbot.modeling_blenderbot import BlenderbotForConditionalGeneration
    from transformers.models.blenderbot.tokenization_blenderbot import BlenderbotTokenizer

    return WhisperProcessor, AutoModelForSpeechSeq2Seq, BlenderbotTokenizer, BlenderbotForConditionalGeneration


@st.cache_resource
def load_models():
    if torch is None:
        raise RuntimeError("PyTorch is not available")
    if librosa is None or np is None or sf is None:
        raise RuntimeError("Audio dependencies are not available")

    try:
        WhisperProcessor, AutoModelForSpeechSeq2Seq, BlenderbotTokenizer, BlenderbotForConditionalGeneration = _load_transformers()
    except Exception as exc:
        raise RuntimeError(f"Transformers models could not be loaded: {exc}") from exc

    whisper_processor = WhisperProcessor.from_pretrained("openai/whisper-tiny.en")
    whisper_model = AutoModelForSpeechSeq2Seq.from_pretrained("openai/whisper-tiny.en").to(DEVICE)

    blender_tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
    blender_model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill").to(DEVICE)

    return {
        "whisper": (whisper_processor, whisper_model),
        "blender": (blender_tokenizer, blender_model),
    }


def speech_to_text(audio_path, processor, model):
    if librosa is None or np is None:
        raise RuntimeError("Audio dependencies are not available")
    speech_array, _ = librosa.load(audio_path, sr=SAMPLE_RATE)
    inputs = processor(np.array(speech_array), sampling_rate=SAMPLE_RATE, return_tensors="pt").to(DEVICE)
    predicted_ids = model.generate(**inputs, max_new_tokens=128, num_beams=3, early_stopping=True)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription.strip()


def get_response_from_model(user_input, tokenizer, model):
    inputs = tokenizer(user_input, return_tensors="pt").to(DEVICE)
    outputs = model.generate(**inputs, max_new_tokens=80, num_beams=3, early_stopping=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.strip()

def speak_response(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name
        tts.save(temp_path)
        audio_bytes = open(temp_path, "rb").read()
    os.remove(temp_path)
    return io.BytesIO(audio_bytes)

def run_voice_assistant(uploaded_file):
    if uploaded_file is None:
        return None, None, "⚠️ Please upload a WAV audio file."

    if uploaded_file.type != "audio/wav":
        return None, None, "⚠️ Please upload a valid WAV audio file."

    try:
        models = load_models()
        whisper_processor, whisper_model = models["whisper"]
        blender_tokenizer, blender_model = models["blender"]

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        data, sr = librosa.load(tmp_path, sr=SAMPLE_RATE)
        sf.write(tmp_path, data, sr)

        command = speech_to_text(tmp_path, whisper_processor, whisper_model)
        reply = get_response_from_model(command, blender_tokenizer, blender_model)
        audio_data = speak_response(reply)

        return audio_data, command, reply

    except Exception as e:
        return None, None, f"⚠️ Voice assistant unavailable: {e}"

