import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class colors:
    header = '\u001b[34m' #BLUE
    assistant = '\033[93m' #YELLOW
    warning = '\033[91m' #RED
    reset = '\033[0m' #RESET COLOR

def itemStyle(breakfast):
    if 'egg' in breakfast or 'eggs' in breakfast:
        eggStyle = input(f'{colors.assistant}\nAey-I: How would you like your eggs? ')
        print(f"{colors.assistant}\nAey-I: {eggStyle}, got it, good choice")
    if 'coffee' in breakfast:
        coffeeChoice = input(f'{colors.assistant}\nAey-I: Would you like cream in your coffee? ').lower()
        if 'yes' in coffeeChoice:
            print(f'{colors.assistant}\nAey-I: One coffee with cream coming right up')
        else:
            print(f'{colors.assistant}\nAey-I: Black coffee it is')

# def addToOrder(breakfast, userResponse):
#     while userResponse == 'yes':
#         extraOrder = input(f'{colors.assistant}\nAey-I: What would you like? ').lower()
#         itemStyle(extraOrder)
#         breakfast.append(extraOrder)
#         userResponse = input(f'{colors.assistant}\nAey-I: Can I get anything else for you? ').lower()



# def breakFastOrder(userBreakfast):
#     breakfast = userBreakfast.split(', ')
#     return breakfast

