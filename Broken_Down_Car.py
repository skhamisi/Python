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

def repairCar():
def buyNewCar():
def buyUsedCar():

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




