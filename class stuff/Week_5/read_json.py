import json

with open("student_scores.json", "r") as file:
    student_scores = json.load(file)

print("The object type is: ", type(student_scores))
print(student_scores)
