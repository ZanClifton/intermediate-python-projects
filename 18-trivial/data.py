import requests

data = requests.get(url="https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean")
data.raise_for_status()

question_data = data.json()["results"]

# 'category': 
# 'type': 
# 'difficulty': 
# 'question': 
# 'correct_answer': 
# 'incorrect_answers': 