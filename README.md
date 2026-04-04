# AI Email Writer (GenAI Project)

A Generative AI-powered web application that creates professional emails based on user input such as topic, tone, and key points.

## Features

* Generate emails using AI
* Multiple email tones:
  * Friendly
  * Formal
  * Professional
  * Apology
  * Follow-up
  * Sales
* Email length options:
  * Short
  * Medium
  * Detailed
* Predefined templates:
  * Leave request
  * Job application
  * Meeting request
  * Follow-up email
  * Complaint email
* Download generated email as TXT
* Simple and interactive UI using Streamlit

## Tech Stack
* Python
* Streamlit (UI)
* OpenAI API / Ollama (LLM)
* dotenv (environment variables)

## Project Structure

AI-Email-Writer/
│
├── app.py                # Streamlit UI
├── email_generator.py   # GenAI logic
├── requirements.txt
├── .env                 
└── README.md