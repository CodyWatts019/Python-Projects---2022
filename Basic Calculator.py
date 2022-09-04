def add(a,b):
    anwser = a+b
    print(str(a) + "+" + str(b) + "=" + str(anwser) + '\n')

def sub(a,b):
    anwser = a-b
    print(str(a) + "-" + str(b) + "=" + str(anwser) + '\n')

def multipication(a,b):
    anwser = a*b
    print(str(a) + "*" + str(b) + "=" + str(anwser) + '\n')

def division(a,b):
    anwser = a/b
    print(str(a) + "/" + str(b) + "=" + str(anwser)+ '\n')
while True:
    print("A. Additiom")
    print("B. Subtraction")
    print("C. Multipication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")

    if choice=="a" or choice=="A":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a,b)

    elif choice =="b" or choice=="B":
        print("Subtract")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        sub(a,b)

    elif choice =="c" or choice=="C":
        print("Multipication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        multipication(a,b)

    elif choice =="d" or choice=="D":
        print("Subtract")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        division(a,b)

    elif choice =="e" or choice=="E":
        print("Program ended.")
        quit()
