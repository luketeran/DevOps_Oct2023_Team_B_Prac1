import math

def arithmetic():
    pass

def trigonometry():
    pass

def exponents():
    pass

def square_root():
    while(True):
        option = sqrt_menu()
        if(option == '0'):
            break
        else:
            print('Value to Square Root')
            try:
                value = float(input('>'))
                print()
                print('Square Root Value is \t')
                print(math.sqrt(value))

            except ValueError:
                print('Please Enter a number:')

def sqrt_menu():#menu to display when the option for the square root function is selected. returns a value that represents the option
    print('\nChoose an Option: ')
    print('1. Input')
    print('0. Exit')
    option = input(">")
    return option

def getPercentage():
    try:
        value = float(input('Enter Value: \n>'))
        totalValue = float(input('Enter Total Value: \n>'))

    except ValueError:
        print('Please Enter a number')
        print('===================================')
    percentage = (value / totalValue) * 100
    print('Percentage Value is ', percentage)

def getValue():
    try:
        totalValue = float(input('Enter Total Value: \n'))
        percentage = float(input('Enter Percentage value: \n'))

    except ValueError:
        print('Please Enter a number')
        print('===================================')

    value = (percentage /100) * totalValue
    print('Value is ', value)

def percentage_Menu():#menu to display when the option for the percentage function is selected. returns a value that represents the option
    while(True):
        print('\nChoose an Option: ')
        print('1. Find Percentage')
        print('2. Find Value of a Percentage')
        print('0. Exit')
        option = input(">")

        if (option == '1'):
            getValue()

        elif(option == '2'):
            getPercentage()

        else:
            break

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
            percentage_Menu()
            break
        elif category == '6':
            return 'exit'
        else:
            print('Please enter a valid input.')

while True:
    if main() == "exit":
        break
