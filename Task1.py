import random
random_num = random.randint(1,10)
user_name = input("What is your name?")
user_number = input("Pick a number between 1 and 10:")
if random_num == user_number:
    print("Well done, " + user_name + "! The number is correct")
else:
    print("Wrong, " + user_name + ", your number is not correct")