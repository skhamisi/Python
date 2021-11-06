#Simple function for clearing backlog of commands from the console
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Monthly operating budget after taxes. Making $10/hr at 30 hours/week at 15% tax rate
preTaxSalary = ((10 * 30) * 4)
tax = preTaxSalary * .15
monthlySalary = preTaxSalary - tax
takeHomeSalary = monthlySalary - 700

#Total cost to repair car
repairCost = 2500
monthlyRepairPayment = round(repairCost / 12) + (repairCost * .17)

#Cost of a new car
newCarPrice = 20000
monthlyNewCarPayment = round(newCarPrice / 12) + (newCarPrice * .10)

#Cost of a used car
usedCarPrice = 9000
monthlyUsedCarPayment = round(usedCarPrice / 12) + (usedCarPrice * .12)

#Function for reapiring current car
def repairCar():
    userChoice = input('''\nYou've chosen to repair your car, are you sure about that?
Type [yes] or [no]\n''')
    if userChoice == 'yes' or userChoice == 'Yes':
        print(f'\nYou make: ${monthlySalary} every month')
        print(f'After paying your current bills, you will have ${takeHomeSalary}')
        print(f'Repairing your car will cost ${repairCost} and add ${monthlyRepairPayment} to your monthly obligations')
        print(f'If you repair your car, you will have ${takeHomeSalary - monthlyRepairPayment} left over very month')
    userChoice = input('''Do you want to proceed with repairing your car?
Type [yes] or [no]\n''')
    if userChoice == 'yes' or userChoice == 'Yes':
        if monthlyRepairPayment > takeHomeSalary:
            print('\nThis is gonna be though, better find another job!')
            input()
            makeAChoice()
        else:
            print('Congrats! Looks like you can afford this!')
            input()
            makeAChoice()
    if userChoice == 'no' or userChoice == 'No':
        makeAChoice()

#Function for buying a new car
def buyNewCar():
    userChoice = input('''\nYou've chosen to  buy a new car, are you sure about that?
Type [yes] or [no]\n''')
    if userChoice == 'yes' or userChoice == 'Yes':
        print(f'\nYou make: ${monthlySalary} every month')
        print(f'After paying your current bills, you will have ${takeHomeSalary}')
        print(f'Buying a new car will cost ${newCarPrice} and add ${monthlyNewCarPayment} to your monthly obligations')
        print(f'If you repair your car, you will have ${takeHomeSalary - monthlyNewCarPayment} left over very month')
    userChoice = input('''Do you want to proceed with repairing your car?
Type [yes] or [no]\n''')
    if userChoice == 'yes' or userChoice == 'Yes':
        if monthlyNewCarPayment > takeHomeSalary:
            print('\nThis is gonna be though, better find another job!')
            input()
            makeAChoice()
        else:
            print('Congrats! Looks like you can afford this!')
            input()
            makeAChoice()
    if userChoice == 'no' or userChoice == 'No':
        makeAChoice()

#Function for buying a used car
def buyUsedCar():
    userChoice = input('''\nYou've chosen to  buy a used car, are you sure about that?
Type [yes] or [no]\n''')
    if userChoice == 'yes' or userChoice == 'Yes':
        print(f'\nYou make: ${monthlySalary} every month')
        print(f'After paying your current bills, you will have ${takeHomeSalary}')
        print(f'Buying a new car will cost ${usedCarPrice} and add ${monthlyUsedCarPayment} to your monthly obligations')
        print(f'If you repair your car, you will have ${takeHomeSalary - monthlyUsedCarPayment} left over very month')
    userChoice = input('''Do you want to proceed with repairing your car?
Type [yes] or [no]\n''')
    if userChoice == 'yes' or userChoice == 'Yes':
        if monthlyUsedCarPayment > takeHomeSalary:
            print('\nThis is gonna be though, better find another job!')
            input()
            makeAChoice()
        else:
            print('Congrats! Looks like you can afford this!')
            input()
            makeAChoice()
    if userChoice == 'no' or userChoice == 'No':
        makeAChoice()

#Presents user with three scenarios concerning their broken car
def makeAChoice():
    cls()
    userDecision = input('''Make a selection
    Enter [1] to repair your car
    Enter [2] to buy a new car
    Enter [3]to buy a used car\n''')
    if userDecision == '1':
        repairCar()
    if userDecision == '2':
        buyNewCar()
    if userDecision == '3':
        buyUsedCar()

makeAChoice()




