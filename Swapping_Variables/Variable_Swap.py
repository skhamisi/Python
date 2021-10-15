print('Enter two numbers to see a magic trick!')
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(f'First number is: {num1} and second number is: {num2}')
input('Press [ENTER] to process numbers')

tempNum = num1
num1 = num2
num2 = tempNum

print('\nPROCESSING....\n')

print(f'First number is now: {num1} and second number is now: {num2}')