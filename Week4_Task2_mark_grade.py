# Task 2
# Write a program to ask a student for their percentage mark and convert this to a grade.
# The conversion will be done in a function called mark_grade


def mark_grade(perc):
    if perc >= 90:
        return "A*"
    elif perc >= 75 and perc < 90:
        return "A"
    elif perc >= 65 and perc < 75:
        return "B"
    elif perc >= 55 and perc < 65:
        return "C"
    elif perc >= 45 and perc <55:
        return "D"
    else:
        return "F"

mark = int(input("What percentage mark did you achive?"))
grade = mark_grade(mark)
print(grade)


# Extension to Task 2•
# Ask the user for their target grade and print this with their mark•
# If their target grade > exam grade display a suitable message•
# If their target grade = exam grade display a suitable message•
# If their target grade < exam grade display a suitable message

target = input("What is your target grade?")

if target == grade:
    print("You achieved your desired grade!")
elif target > grade:
    print("You got a higher gradew than your target grade!")
else:
    print("You need to work harder")

