number_1 = int(input("Select a number"))
number_2 = int(input("Select a second number"))
print('Enter "a" if you want to add')
print('Enter "b" if you want to subtract')
print('Enter "c" if you want to divide')
print('Enter "d" if you want to multiply')
print('Enter "e" if you want to raise to the power')
operator = input("Select an operator")
if operator == "a":
    print(number_1 + number_2)
elif operator =="b":
    print(number_1 - number_2)
elif operator == "c":
    print(number_1 / number_2)
elif operator == "d":
    print(number_1 * number_2)
elif operator == "e":
    print(number_1 ** number_2)