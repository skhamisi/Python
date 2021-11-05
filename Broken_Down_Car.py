#Monthly operating budget after taxes
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

#Runs function for reapiring current car
def repairCar():
    userChoice = input("You've chosen to repair your car, are you sure about that?")
    if userChoice == 'yes' or userChoice == 'Yes':
        print(f'You make: {monthlySalary} every month')
        print(f'After paying your current bills, you will have {takeHomeSalary}')
        print(f'Repairing your car will cost {repairCost} and add {monthlyRepairPayment} to your monthly bills')
        print(f'If you repair your car, you will have {takeHomeSalary - monthlyRepairPayment}')
#Run function for buying a new car
def buyNewCar():

#Runs function for buying a used car
def buyUsedCar():

#Presents user with three scenarios concerning their broken car
def makeAChoice():
    userChoice = input('''Make a selection
    Enter [1] to repair your car
    Enter [2] to buy a new car
    Enter [3]to buy a used car ''')
    if userChoice == 1:
        repairCar()
    if userChoice == 2:
        buyNewCar()
    if userChoice == 3:
        buyUsedCar()

makeAChoice()




