more_students = ["Sonja", "Melissa", "Karen"]
file = open("output_file.txt", "a")
file.write("Here are some more names:\n")

for s in more_students:
    file.write(s + "\n")

file.close()
