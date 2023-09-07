# steps of code
# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit


def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")


def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")


def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")


def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")


def power(a, b):
    answer = a**b
    print(str(a) + " ** " + str(b) + " = " + str(answer) + "\n")


while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplicaton")
    print("D. Division")
    print("E. a Power of b")
    print("F. Exit")

    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("enter your first number: "))
        b = int(input("enter your second number: "))
        add(a, b)

    elif choice == "b" or choice == "B":
        print("Substraction")
        a = int(input("enter your first number: "))
        b = int(input("enter your second number: "))
        sub(a, b)

    elif choice == "c" or choice == "C":
        print("Substraction")
        a = int(input("enter your first number: "))
        b = int(input("enter your second number: "))
        mul(a, b)

    elif choice == "d" or choice == "D":
        print("MUltiplication")
        a = int(input("enter your first number: "))
        b = int(input("enter your second number: "))
        div(a, b)

    elif choice == "e" or choice == "E":
        print("a power of b")
        a = int(input("enter your first number: "))
        b = int(input("enter your second number: "))
        power(a, b)

    elif choice == "f" or choice == "F":
        print("Exit")
        quit()

    else:
        print("please choose from A to F only")
