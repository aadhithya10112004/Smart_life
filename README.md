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

Add screenshot here.

### Dashboard

Add screenshot here.

### AI Assistant

Add screenshot here.

### News Summarizer

Add screenshot here.

### PDF Summarizer

Add screenshot here.

### Mood Tracker

Add screenshot here.

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

Computer Science Engineering Student

GitHub: https://github.com/aadhithya10112004

---

## License

This project is licensed under the MIT License.
