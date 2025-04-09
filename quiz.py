from fastapi import FastAPI
import json
import random

app = FastAPI()

# Load quiz data from JSON file
with open("quiz_data.json", "r", encoding="utf-8") as f:
    quiz_data = json.load(f)

@app.get("/quiz/")
def get_quiz():
    """Returns a random quiz question."""
    question = random.choice(quiz_data)
    return {
        "id": question["id"],
        "meaning": question["meaning"],
        "kanji": question["kanji"],
        "options": question["options"]
    }

@app.post("/check_answer/")
def check_answer(quiz_id: int, user_answer: str):
    """Checks if the user's answer is correct."""
    question = next((q for q in quiz_data if q["id"] == quiz_id), None)
    if question:
        return {"correct": user_answer == question["kanji"]}
    return {"error": "Invalid quiz ID"}

# uvicorn quiz:app --reload