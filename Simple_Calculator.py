import math

def arithmetic():
    pass

def trigonometry():
    pass

def exponents():
    pass

def square_root():
    pass

def percentage():
    pass

def main_menu():
    print('\nChoose a category of operation:')
    print('1. Standard Arithmetic')
    print('2. Trigonometry')
    print('3. Exponents')
    print('4. Square Root')
    print('5. Percentage')
    print('6. Exit')

def main():
    main_menu()
    while True: #to display the menu only once
        category = input("> ")
        if category == '1':
            arithmetic()
            break
        elif category == '2':
            trigonometry()
            break
        elif category == '3':
            exponents()
            break
        elif category == '4':
            square_root()
            break
        elif category == '5':
            percentage()
            break
        elif category == '6':
            return 'exit'
        else:
            print('Please enter a valid input.')

while True:
    if main() == "exit":
        break
