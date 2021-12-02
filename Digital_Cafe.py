#Digital Cafe
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class colors:
    header = '\u001b[34m' #BLUE #BOLD #UNDERLINE
    assistant = '\033[93m' #YELLOW
    warning = '\033[91m' #RED
    reset = '\033[0m' #RESET COLOR

cls()

print(f'''{colors.header}Welcome to the Digital Cafe
---------------------------\n''')

print(f"{colors.assistant}Hi, my name is Aey-I, I'll be your sever today. What can I get started for you?\n")
print(f'''{colors.reset}Enter your order below
*NOTE: Please put a comma in between each item\n''')

userBreakfast = input().lower()

breakfast = userBreakfast.split(', ')

if 'egg' in breakfast or 'eggs' in breakfast:
    eggStyle = input(f'{colors.assistant}\nAey-I: How would you like your eggs? ')
    print(f"\nAey-I: {eggStyle}, got it, good choice\n")
if 'coffee' in breakfast:
    coffeeChoice = input('Aey-I: Would you like cream in your coffee? ').lower()
    if 'yes' in coffeeChoice:
        print('\nAey-I: One coffee with cream coming right up')
    else:
        print('\nAey-I: Black coffee it is\n')

userResponse = input('\Aey-I: Can I get anything else for you? ').lower()
# if 'yes' in userResponse:
#     extraOrder = input('\nAttendant: What would you like? ').lower()
#     breakfast.append(extraOrder)

while 'yes' in userResponse:
    extraOrder = input('\Aey-I: What would you like? ').lower()
    breakfast.append(extraOrder)
    userResponse = input('\Aey-I: Can I get anything else for you? ').lower()
    

print('\Aey-I: I got your order as')
print(*breakfast, sep = "\n")

userReply = input('\Aey-I: Did I miss anything? ').lower()
if 'yes' in userReply:
    forgottenOrder = input('\Aey-I: What did I miss? ').lower()
    breakfast.append(forgottenOrder)
    print(f'Aey-I: Sorry about that, I added {forgottenOrder} to your order')

print("\Aey-I: Thanks! we'll have your order out right away")
