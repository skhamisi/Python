#Digital Cafe
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

print("\nWelcome to the Digital Cafe, what can I get started for you?")

print('''Enter your order below
*NOTE: Please put a comma in between each item\n''')

userBreakfast = input().lower()

breakfast = userBreakfast.split(', ')

if 'egg' in breakfast or 'eggs' in breakfast:
    eggStyle = input('\nHow would you like your eggs? ')
    print(f"\nAttendant: {eggStyle}, got it, good choice\n")
if 'coffee' in breakfast:
    coffeeChoice = input('Attendant: Would you like cream in your coffee? ').lower()
    if 'yes' in coffeeChoice:
        print('\nAttendant: One coffee with cream coming right up')
    else:
        print('\nAttendant: Black coffee it is\n')

userResponse = input('\nAttendant: Can I get anything else for you? ').lower()
# if 'yes' in userResponse:
#     extraOrder = input('\nAttendant: What would you like? ').lower()
#     breakfast.append(extraOrder)

while 'yes' in userResponse:
    extraOrder = input('\nAttendant: What would you like? ').lower()
    breakfast.append(extraOrder)
    userResponse = input('\nAttendant: Can I get anything else for you? ').lower()
    

print('\nAttendant: I got your order as')
print(*breakfast, sep = "\n")

userReply = input('\nAttendant: Did I miss anything? ').lower()
if 'yes' in userReply:
    forgottenOrder = input('\nAttendant: What did I miss? ').lower()
    breakfast.append(forgottenOrder)
    print(f'Attendant: Sorry about that, I added {forgottenOrder} to your order')

print("\nAttendant: Thanks! we'll have your order out right away")
