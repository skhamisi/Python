import random

#Function for addition arithmetic, takes one parameter 'numProb' which holds the value for the number of problems the user chose 
def RunAddition(numProb):
    print(f'\nYou are testing on addition and you have {numProb} problems')

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
        userAnswer = int(input(f'{one} + {two} = '))

        #User input is checked against the value stored in 'answer', if true the 'score' variable is incremented
        if answer == userAnswer:
            print('Correct')
            score += 1
        #If user input is not correct, the 'score' variable is not incremented
        else:
            print('Incorrect')
            print(f'Correct answer is {answer}')
        #At the end of the loop, our 'numProd' varibale is decremented, once this reaches zero the while loop will stop generating problems
        numProb -= 1
    #'score' is divided by 'prob' and then multiplied by 100 in order to present a test score to the user 
    print(f'\nYou got {score} out {prob} correct, your score is {(score/prob) * 100}')

#Function for subtraction arithmetic 
def RunSubtraction(numProb):
    print(f'\nYou are testing on subtraction and you have {numProb} problems')
    prob = numProb
    score = 0

    while(numProb > 0):
        one = random.randint(1,20)
        two =  random.randint(1,20)
        answer = one - two

        userAnswer = int(input(f'{one} - {two} = '))

        if answer == userAnswer:
            print('Correct')
            score += 1
        else:
            print('Incorrect')
            print(f'Correct answer is {answer}')
        numProb -= 1
    print(f'\nYou got {score} out {prob} correct, your score is {(score/prob) * 100}')

#Function for multiplication arithmetic 
def RunMultiplication(numProb):
    print(f'\nYou are testing on multiplication and you have {numProb} problems')
    prob = numProb
    score = 0

    while(numProb > 0):
        one = random.randint(1,13)
        two =  random.randint(1,20)
        answer = one * two

        userAnswer = int(input(f'{one} x {two} = '))

        if answer == userAnswer:
            print('Correct')
            score += 1
        else:
            print('Incorrect')
            print(f'Correct answer is {answer}')
        numProb -= 1
    print(f'\nYou got {score} out {prob} correct, your score is {(score/prob) * 100}')

#Function for division arithmetic 
def RunDivision(numProb):
    print(f'\nYou are testing on Division and you have {numProb} problems')
    prob = numProb
    score = 0

    while(numProb > 0):
        one = random.randint(1,13)
        two =  random.randint(1,13)
        answer= one / two

        userAnswer = float(input(f'{one} / {two} = '))
        difference = abs(userAnswer - answer)

        if difference < .05:
            print('Correct')
            score += 1
        else:
            print('Incorrect')
            print(f'Correct answer is {answer}')
        numProb -= 1
    print(f'\nYou got {score} out {prob} correct, your score is {(score/prob) * 100}')  

def checkValidInput(selection):
    while selection > 4 or selection <=0:
        print('Invalid choice, please try again')
        selection = int(input('Choose a math category: '))
        checkValidInput(selection)
    return selection