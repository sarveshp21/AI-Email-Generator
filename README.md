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

```
ai-email-writer/
│
├── app.py                # Streamlit UI
├── email_generator.py   # GenAI logic
├── requirements.txt
├── .env                 # API key (not pushed to GitHub)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/ai-email-writer.git
cd ai-email-writer
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file and add:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run the app

```
streamlit run app.py
```

---

## 🌐 Deployment

You can deploy this app using:

* Streamlit Community Cloud
* Render
* HuggingFace Spaces

---

## 📸 Screenshots

(Add screenshots of your app here)

---

## 📌 Future Improvements

* Add PDF download support
* Add email copy button
* Improve UI design
* Add history of generated emails
* Switch between OpenAI and local LLM (Ollama)

---

## 🤝 Contributing

Feel free to fork the repo and contribute.

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/your-username
