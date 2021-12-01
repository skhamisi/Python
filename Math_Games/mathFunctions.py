import random, os


totalTestsTaken = 0
testAvg = 0
addRunAvg = 0
subRunAvg = 0
multRunAvg = 0
divRunAvg = 0

#Keeps track of number of individual tests taken
addTestsTaken = 0
subTestsTaken = 0
multTestsTaken = 0
divTestsTaken = 0

class colors:
    header = '\u001b[34m' #BLUE #BOLD #UNDERLINE
    default = '\033[93m' #YELLOW
    correct = '\033[92m' #GREEN
    wrong = '\033[91m' #RED
    reset = '\033[0m' #RESET COLOR

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Function for addition arithmetic, takes one parameter 'numProb' which holds the value for the number of problems the user chose 
def RunAddition(numProb):
    cls()
    print(f'{colors.reset}\nYou are testing on addition and you have [{numProb}] problem(s)')
    input(f'{colors.default}Press [ENTER] to continue\n')

    #the value of 'numProb' is assigned to 'prob' in order to seperate the variables for the purpose of scoring at the end of the test
    prob = numProb
    score = 0

    #The while loop takes the number of problems the user specified and keeps generating problems until the condition evaluates to false
    while(numProb > 0):
        #the random.randint generates random numbers between 1, 20
        one = random.randint(1,20)
        two =  random.randint(1,20)
        #Here the actual arithemtic is processed and the value assigned to 'answer'
        answer = one + two

        #The generated numbers are presented to the user and their input recorded
        userAnswer = int(input(f'{colors.reset}{one} + {two} = '))

        #User input is checked against the value stored in 'answer', if true the 'score' variable is incremented
        if answer == userAnswer:
            print(f'{colors.correct}Correct\n')
            score += 1
        #If user input is not correct, the 'score' variable is not incremented
        else:
            print(f'{colors.wrong}Incorrect')
            print(f'Correct answer is {answer}\n')
        #At the end of the loop, our 'numProd' varibale is decremented, once this reaches zero the while loop will stop generating problems
        numProb -= 1
    #'score' is divided by 'prob' and then multiplied by 100 in order to present a test score to the user
    userScore = (score/prob) * 100
    print(f'{colors.reset}You got {score} of {prob} correct, your score is {userScore}')
    global addRunAvg
    global addTestsTaken
    addRunAvg += userScore
    addTestsTaken += 1

#Function for subtraction arithmetic 
def RunSubtraction(numProb):
    cls()
    print(f'{colors.reset}\nYou are testing on subtraction and you have [{numProb}] problem(s)')
    input(f'{colors.default}Press [ENTER] to continue\n')
    prob = numProb
    score = 0

    while(numProb > 0):
        one = random.randint(1,20)
        two =  random.randint(1,20)
        answer = one - two

        userAnswer = int(input(f'{colors.reset}{one} - {two} = '))

        if answer == userAnswer:
            print(f'{colors.correct}Correct\n')
            score += 1
        else:
            print(f'{colors.wrong}Incorrect')
            print(f'Correct answer is {answer}\n')
        numProb -= 1
    userScore = (score/prob) * 100
    print(f'{colors.reset}You got {score} of {prob} correct, your score is {userScore}')
    global subRunAvg
    global subTestsTaken
    subRunAvg += userScore
    subTestsTaken += 1

#Function for multiplication arithmetic 
def RunMultiplication(numProb):
    cls()
    print(f'{colors.reset}\nYou are testing on multiplication and you have [{numProb}] problem(s)')
    input(f'{colors.default}Press [ENTER] to continue\n')
    prob = numProb
    score = 0

    while(numProb > 0):
        one = random.randint(1,13)
        two =  random.randint(1,13)
        answer = one * two

        userAnswer = int(input(f'{colors.reset}{one} x {two} = '))

        if answer == userAnswer:
            print(f'{colors.correct}Correct\n')
            score += 1
        else:
            print(f'{colors.wrong}Incorrect')
            print(f'Correct answer is {answer}\n')
        numProb -= 1
    userScore = (score/prob) * 100
    print(f'{colors.reset}You got {score} of {prob} correct, your score is {userScore}')
    global multRunAvg
    global multTestsTaken
    multRunAvg += userScore
    multTestsTaken += 1

#Function for division arithmetic 
def RunDivision(numProb):
    cls()
    print(f'{colors.reset}\nYou are testing on Division and you have [{numProb}] problem(s)')
    input(f'{colors.default}Press [ENTER] to continue\n')
    prob = numProb
    score = 0

    while(numProb > 0):
        one = random.randint(1,13)
        two =  random.randint(1,13)
        answer= one / two

        userAnswer = float(input(f'{colors.reset}{one} / {two} = '))

        #The Python abs() method takes the absolute value of the number derived from 'userAnswer' minus 'answer' and assigns that value to 
        #difference'
        difference = abs(userAnswer - answer)

        #If the value stored in 'difference' is less than .05, then the user answer is presented as correct 
        if difference < .05:
            print(f'{colors.correct}Correct\n')
            score += 1
        else:
            print(f'{colors.wrong}Incorrect')
            print(f'Correct answer is {answer}\n')
        numProb -= 1
    userScore = (score/prob) * 100
    print(f'{colors.reset}You got {score} of {prob} correct, your score is {userScore}')
    global divRunAvg
    global divTestsTaken
    divRunAvg += userScore
    divTestsTaken += 1 

#A method for error handling user input when the user chooses a category in the main menu
def checkValidInput(selection):
    #As long as the user selection is greater than 4 or less than or equal to zero, the user is presented with an error message. 
    while selection > 4 or selection <=0:
        print('Invalid choice, please try again')
        selection = int(input('Choose a math category: '))
        checkValidInput(selection)
    #If user input falls between the parameters, the while loop is never initiated and the code continues to execute
    return selection

#Displays the initial menu to the user where they can choose a category
def MathTest():
    cls()
    global totalTestsTaken
    print(f'{colors.header}Number of tests taken: {totalTestsTaken}\n')

    print(f'{colors.reset}Welcome to Math Games!')
    print('======================')
    print('''
    Enter [1] for addition
    Enter [2] for subtraction
    Enter [3] for multiplication 
    Enter [4] for division''')

    userInput = int(input(f'{colors.default}\nChoose a math category: '))

    #userInput is passed to 'checkValidInput' to make sure the value ranges from 1-4
    userInput = checkValidInput(userInput)

    if userInput == 1:
        userChoice = int(input('\nHow many problems would you like to solve? '))
        RunAddition(userChoice)
    if userInput == 2:
        userChoice = int(input('\nHow many problems would you like to solve? '))
        RunSubtraction(userChoice)
    if userInput == 3:
        userChoice = int(input('\nHow many problems would you like to solve? '))
        RunMultiplication(userChoice)
    if userInput == 4:
        userChoice = int(input('\nHow many problems would you like to solve? '))
        RunDivision(userChoice)
    
    #Increments counter to keep track of test attempts
    totalTestsTaken += 1

    #Keeps track of final user average for addition tests
    if addTestsTaken > 0:
        finalAddAvg = round(addRunAvg/addTestsTaken)
    if subTestsTaken > 0:
        finalSubAvg = round(subRunAvg/subTestsTaken)
    if multTestsTaken > 0:
        finalMultAvg = round(multRunAvg/multTestsTaken)
    if divTestsTaken > 0:
        finalDivAvg = round(divRunAvg/divTestsTaken)

    print('\nWould you like to practice another test?')
    userInput = input(f'{colors.default}Enter [yes] to continue or [no] to quit: ')
    userInput = userInput.lower()

    if userInput == 'yes':
        #totalTestsTaken +=1
        MathTest()
    else:
        if addTestsTaken > 0:
            print (f'{colors.reset}\nYour average score for Addition is {finalAddAvg}')
        if subTestsTaken > 0:
            print (f'\nYour average score for Subtraction is {finalSubAvg}')
        if multTestsTaken > 0:
            print (f'\nYour average score for Multiplication is {finalMultAvg}')
        if divTestsTaken > 0:
            print (f'\nYour average score for Division is {finalDivAvg}')
        exit()