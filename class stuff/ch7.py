#today = "Saturday"
code_days = ["Tuesday", "Thursday"]
scrum_days = ["Monday", "Wednesday", "Friday"]

today = input("what day is it? ")
if today in code_days:
    print("We write Code")
elif today in scrum_days:
    print("Time to learn Scrum!")
else:
    print ("Time to relax")
