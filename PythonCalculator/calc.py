###################Python Calculator######################
#This is only a simple calculator, only supports two numbers for different operations

#Math module import
import math
#Import os
import os

def mathOperation():
    os.system('cls')
    currentOp = None
    #Ask for desired math operation
    print('Please select operation using the corresponding number:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Power')
    print('6. Square Root')
    chosenNum = input('Enter the corresponding Number: \n')

    if chosenNum == '1':
        currentOp = 'Addition'
        print('The chosen operation is ' + currentOp)
        num1 = input('Input the first number: \n')
        num2 = input('Input the second number: \n')
        answer = float(num1) + float(num2)
        print(answer);
        input('Press Enter to continue \n')
        os.system('cls')
        mathOperation()

    elif chosenNum == '2':
        currentOp = 'Subtraction'
        print('The chosen operation is ' + currentOp)
        num1 = input('Input the subtrahend: \n')
        num2 = input('Input the difference: \n')
        answer = float(num1) - float(num2)
        print(answer);
        input('Press Enter to continue \n')
        os.system('cls')
        mathOperation()

    elif chosenNum == '3':
        currentOp = 'Multiplication'
        print('The chosen operation is ' + currentOp)
        num1 = input('Input the first number: \n')
        num2 = input('Input the second number: \n')
        answer = float(num1) * float(num2)
        print(answer);
        input('Press Enter to continue \n')
        os.system('cls')
        mathOperation()

    elif chosenNum == '4':
        currentOp = 'Division'
        print('The chosen operation is ' + currentOp)
        num1 = input('Input the dividend: \n')
        num2 = input('Input the divisor: \n')
        answer = float(num1) / float(num2)
        print(answer)
        input('Press Enter to continue \n')
        os.system('cls')
        mathOperation()

    elif chosenNum == '5':
        currentOp = 'Power'
        print('The chosen operation is ' + currentOp)
        num1 = input('Input the base number: \n')
        num2 = input('Input the exponent: \n')
        answer = math.pow(float(num1), float(num2))
        print(answer)
        input('Press Enter to continue \n')
        os.system('cls')
        mathOperation()

    elif chosenNum == '6':
        currentOp = 'Square Root'
        print('The chosen operation is ' + currentOp)
        num1 = input('Input the radicand: \n')
        answer = math.sqrt(float(num1))
        print(answer)
        input('Press Enter to continue \n')
        os.system('cls')
        mathOperation()

#Call mathOperation function
mathOperation()
