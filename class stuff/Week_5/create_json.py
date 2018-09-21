import json

student_scores = {"name": "John", "scores": [90, 88, 92]}
with open("student_scores.json", "w") as file:
    json.dump(student_scores, file)
