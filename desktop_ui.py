import tkinter as tk
from tkinter import ttk  # For Table UI
import requests
import json
import os

API_URL = "http://127.0.0.1:8000/quiz/"
SCORE_FILE = "./score_data.json"

# Function to reset scores (only stores wrong answers)
def reset_scores():
    """Clears all previous wrong answers."""
    return {}

# Save scores (overwrite existing file)
def save_scores(scores):
    with open(SCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=4)

# Reset scores at startup (empty wrong answers)
scores = reset_scores()
save_scores(scores)

total_correct = 0
total_wrong = 0

def update_score_label():
    score_label.config(text=f"Score: ✅ {total_correct} | ❌ {total_wrong}")

def update_score_table():
    """Updates the table with only the wrong answers."""
    for row in table.get_children():
        table.delete(row)  # Clear old data

    for kanji, data in scores.items():
        table.insert("", "end", values=(kanji, data["meaning"], data["wrong"]))

def get_new_question():
    response = requests.get(API_URL)
    if response.status_code == 200:
        global question
        question = response.json()

        # Update UI with new question
        label.config(text=question["meaning"])
        for i, btn in enumerate(buttons):
            btn.config(text=question["options"][i], command=lambda ans=question["options"][i]: check_answer(ans))

def check_answer(answer):
    global total_correct, total_wrong
    correct_answer = question["kanji"]
    
    if answer == correct_answer:
        result = "Correct! ✅"
        total_correct += 1
    else:
        result = f"Wrong! ❌ Correct: {correct_answer}"

        # Store wrong answer with meaning
        scores.setdefault(correct_answer, {"meaning": question["meaning"], "wrong": 0})
        scores[correct_answer]["wrong"] += 1  # Track how many times it's wrong
        total_wrong += 1

    save_scores(scores)
    result_label.config(text=result)
    update_score_label()
    update_score_table()  # Refresh table with wrong answers
    get_new_question()

# GUI setup
root = tk.Tk()
root.title("Hanja Quiz")

# Question Label
label = tk.Label(root, text="Press Start to Begin", font=("맑은 고딕", 26))
label.pack(pady=10)

# Option Buttons
buttons = [tk.Button(root, text="", font=("Arial", 24)) for _ in range(4)]
for btn in buttons:
    btn.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 24))
result_label.pack(pady=10)

# Score Label
score_label = tk.Label(root, text=f"Score: ✅ {total_correct} | ❌ {total_wrong}", font=("Arial", 24))
score_label.pack(pady=5)

# Score Table (Treeview) for Wrong Answers
frame = tk.Frame(root)
frame.pack(pady=10)

table = ttk.Treeview(frame, columns=("Kanji", "Meaning", "Wrong"), show="headings", height=20)
table.heading("Kanji", text="Kanji")
table.heading("Meaning", text="Meaning")
table.heading("Wrong", text="❌ Times Wrong")

table.column("Kanji", width=150)
table.column("Meaning", width=350)
table.column("Wrong", width=120)

table.pack()

# Load initial scores into the table (empty at first)
update_score_table()

# Start Quiz Button
start_button = tk.Button(root, text="Start Quiz", command=get_new_question)
start_button.pack(pady=10)

# Run the GUI
root.mainloop()
