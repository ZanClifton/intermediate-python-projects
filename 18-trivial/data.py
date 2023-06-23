import requests

parameters = {
    "amount": 10,
    "category": 9,
    "difficulty": "easy",
    "type": "boolean",
}

URL = f"https://opentdb.com/api.php?amount={parameters['amount']}&category={parameters['category']}&difficulty={parameters['difficulty']}&type={parameters['type']}"

data = requests.get(url=URL)
data.raise_for_status()

question_data = data.json()["results"]

# 'category': 
# 'type': 
# 'difficulty': 
# 'question': 
# 'correct_answer': 
# 'incorrect_answers': 