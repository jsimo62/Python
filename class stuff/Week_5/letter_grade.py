num = int(input("Enter your numeric grade: "))
if num >= 90:
  letter_grade = 'A'
elif num >= 80:
  letter_grade = 'B'
elif num >= 70:
  letter_grade = 'C'
elif num >= 60:
  letter_grade = 'D'
else:
  letter_grade = 'F'

print("Your letter grade is " + letter_grade )
