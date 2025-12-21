import requests

response = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=multiple')
data = response.json()

question_data = []

# Add questions from the API
for question in data["results"]:
    question_data.append({
        "text": question["question"],
        "answer": question["correct_answer"]
    })