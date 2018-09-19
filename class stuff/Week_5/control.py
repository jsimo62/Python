today = "Saturday"
code_days = ["Tuesday", "Thursday"]
scrum_days = ["Monday", "Wednesday", "Friday"]

if today in code_days:
  print("We get to write code!")
elif today in scrum_days:
  print("Time to learn Scrum!")
else:
  print("Time to relax!")
