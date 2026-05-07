# 🤖 AI Chatbot — Groq Powered

A modern AI-powered chatbot built using **Python, Flask, HTML, CSS, and JavaScript**, integrated with the **Groq API** for lightning-fast conversational responses.

🌐 Live Demo: *https://ai-chatbot-mgao.onrender.com/*

📦 GitHub Repo: *https://github.com/harshskarki/ai-chatbot*

---

## ✨ Features

* 🧠 Real AI conversations using Groq API
* 💬 ChatGPT-like interaction experience
* ⚡ Ultra-fast responses with LLaMA 3 models
* 🗂️ Conversation memory using Flask sessions
* 🎨 Clean and responsive UI
* ⌨️ Press Enter to send messages
* 🔐 Secure API key handling with `.env`
* 🌍 Deploy-ready with Render

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### AI Integration

* Groq API
* LLaMA 3.1 Model

### Deployment

* Render
* GitHub

---

## 📂 Project Structure

```bash
ai-chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ai-chatbot.git
cd ai-chatbot
```

---

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

### 5️⃣ Run the Application

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

## 🌐 Deployment (Render)

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

---

## 📸 Screenshots

### 💬 Chat Interface

*Add screenshots here*

---

## 🔥 Future Improvements

* 🗂️ Chat history storage
* 🔐 User authentication
* 🎤 Voice assistant support
* 🌙 Dark/Light mode
* ⚡ Streaming AI responses
* 📱 Mobile-first responsive UI

---

## 🧠 What I Learned

Through this project, I learned:

* Flask backend development
* REST API handling
* AI API integration
* Git & GitHub workflow
* Deployment using Render
* Environment variable security
* Debugging real-world deployment issues

---

## 👨‍💻 Author

### Harshvardhan Singh Karki

B.Tech 3rd Year — CSMU

Experience:

* AI Development
* Full Stack Web Development
* Modern UI/UX
* Building real-world projects

---

## ⭐ Support

If you liked this project:

* ⭐ Star the repository
* 🍴 Fork the project
* 📢 Share it with others

---

## 📜 License

This project is licensed under the MIT License.
