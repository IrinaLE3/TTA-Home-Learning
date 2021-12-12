# Task 1
# Write a program that allows you to enter 4 numbers and stores them in a file called “Numbers” 
# •3•45•83•21
# Have a go at ‘w’ ‘r’ ‘a’


my_file = open("Numbers.txt", "w")
for i in range(4):
    number = input("Enter a number:")
    my_file.write(number)
    my_file.write("\n")
my_file.close()

my_file = open("Numbers.txt", "a")
my_file.write("Additional numbers")
my_file.close()


with open("Numbers.txt","r") as file1:
    data = file1.read()
file1.close()
print(data)

