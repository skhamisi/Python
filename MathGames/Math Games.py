#Application
#-----------
#Simple math test algorithm. Allows for addition, multiplication, and division questions
#Allows for custom number of questions and will give user a score on a scale of 0-100.

#Requirements
#------------
#1) Take user input for one of 4 categories to choose from : Addition, subtraction, multiplication, and division
#2) Allow user input for custom number of problems
#3) Build functions for addition, subtraction, multiplication, and division arithmetic
#4) Provide generation for random set of numbers between a set interval
#5) Build function for displaying correct or incorrect answer to user
#6) Keep track of correct/incorrect answers to provide user with a score

#Imports the methods from a seperate file named 'mathFunctions', seperating the code helps keep it clean and more readable
import mathFunctions as mf

#Displays the initial menu to the user where they can choose a category
print('Welcome to Math Games!')
print('======================')
print('''
Enter [1] for addition
Enter [2] for subtraction
Enter [3] for multiplication 
Enter [4] for division''')

userInput = int(input('\nChoose a math category: '))

#userInput is passed to 'checkValidInput' to make sure the value ranges from 1-4
userInput = mf.checkValidInput(userInput)

#This set of if statments takes the value returned from 'checkValiInput' and runs the correct method selected by the user
if userInput == 1:
    userChoice = int(input('\nHow many problems would you like to solve? '))
    mf.RunAddition(userChoice)
if userInput == 2:
    userChoice = int(input('\nHow many problems would you like to solve? '))
    mf.RunSubtraction(userChoice)
if userInput == 3:
    userChoice = int(input('\nHow many problems would you like to solve? '))
    mf.RunMultiplication(userChoice)
if userInput == 4:
    userChoice = int(input('\nHow many problems would you like to solve? '))
    mf.RunDivision(userChoice)

