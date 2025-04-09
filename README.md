
# 🧠 Hanja Quiz Desktop App (Tkinter + FastAPI)

This project is a desktop application for learning and memorizing Hanja (Chinese characters used in Korean). It includes a Python-based GUI using Tkinter and a FastAPI backend to serve quiz questions.

---
![image](https://github.com/user-attachments/assets/fcb10343-1725-4e0f-a764-e2b917ab550b)

## 📁 Project Structure

```
Quiz/
├── quiz_data.json      # Quiz questions (generated)
├── score_data.json     # Stores only wrong answers (auto-generated)
├── quiz.py             # FastAPI server to serve random quiz questions
├── desktop_ui.py       # Tkinter-based desktop GUI
├── readme.md           # This file
```

---

## 🧪 Step-by-Step: How to Run the Desktop App

### ✅ 1. Install Requirements
Install dependencies if you haven't already:

```bash
pip install fastapi uvicorn requests
```

---

### ✅ 2. Start the FastAPI Server

In the terminal, run:

```bash
uvicorn quiz:app --reload
```

This should output:

```
Uvicorn running on http://127.0.0.1:8000
```

The server serves a random quiz from `quiz_data.json`.

---

### ✅ 3. Run the Desktop GUI (Tkinter)

In a **separate terminal**, run:

```bash
python desktop_ui.py
```

This launches the quiz window. The GUI:
- Loads a random quiz question from the FastAPI server.
- Displays four choices.
- Tells you if you're right or wrong.
- Records only wrong answers in `score_data.json`.

---

## 💡 Features

- Randomized multiple-choice quizzes
- Offline-ready (after server starts)
- Score tracking
- Wrong-answer review table
- Fully written in Python (no web browser needed)

---

## 🧠 Bonus Tip

If you want to reset your mistakes history, simply delete or clear:

```bash
score_data.json
```

---

## 📱 Want a mobile version?

This same app was also ported to Flutter for Android!
Ask `@yourself` how to build the APK 😉.

---

Happy studying!
