# SmartLife

An AI-powered personal wellness platform that combines intelligent health assistance, document summarization, news analysis, productivity tools, and voice interaction into a single application.

---

## Overview

SmartLife is a web application built using Python and Streamlit that helps users improve productivity and well-being through AI-powered features. The application integrates multiple services, including document summarization, intelligent news analysis, YouTube search, diet recommendations, mood tracking, and voice interaction.

The project demonstrates the integration of Large Language Models (LLMs), third-party APIs, and a responsive user interface to deliver a personalized digital wellness experience.

---

## Features

- Secure user authentication
- AI-powered chatbot using Groq
- News search and AI summarization
- YouTube video search
- PDF document summarization
- Voice input support
- Mood tracking
- Diet recommendation system
- Daily task management
- User-friendly Streamlit interface

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Framework | Streamlit |
| Database | SQLite |
| AI Model | Groq LLM |
| APIs | NewsAPI, SerpAPI, YouTube Data API |
| Environment | Python Dotenv |
| PDF Processing | PyPDF2 |
| Speech Recognition | SpeechRecognition |

---

## Project Structure

```
SmartLife/
│
├── assets/
├── data/
├── db/
├── tools/
├── ui/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/SmartLife.git
```

### Navigate to the project

```bash
cd SmartLife
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root and add the following keys.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
NEWS_API_KEY=YOUR_NEWS_API_KEY
SERPAPI_API_KEY=YOUR_SERPAPI_API_KEY
YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will start on:

```
http://localhost:8501
```

---

## Screenshots

### Login Page

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8ff60bcd-c89c-4f16-a3ca-1d67ba62aca7" />


### Dashboard

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d30264a2-9f96-47ff-adbc-e207563c397f" />


### Task Manger

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3b0af173-45e0-4b2b-927a-fac6fc941602" />


### News Summarizer

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f8175ffd-964e-4507-87ed-1a8c139f32b5" />


### PDF Summarizer

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/da8728f2-ef92-4ed5-8627-545674dfa30a" />


### Mood Tracker

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5c8a173b-2883-4e7e-859d-7696bd44863e" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f25ec531-8b57-4ffb-b79d-857940a58784" />


---

## Future Enhancements

- Google Authentication
- Cloud Deployment
- Mobile Application
- Calendar Integration
- Reminder Notifications
- Personalized Health Reports
- Multi-language Support

---

## Author

**Aadhithya S**


GitHub: https://github.com/aadhithya10112004

---

## License

This project is licensed under the MIT License.
