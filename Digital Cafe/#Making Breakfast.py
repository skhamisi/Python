#Digital Cafe

print("\nWelcome to the Digital Cafe, what can I get started for you?")
print('*NOTE: Please put a comma in between each item\n')

userBreakfast = input()

breakfast = userBreakfast.split(', ')

if 'egg' in breakfast or 'eggs' in breakfast:
    eggStyle = input('\nHow would you like your eggs? ')
    print(f"\nAttendant: {eggStyle}, got it, good choice\n")
if 'coffee' in breakfast or 'Coffee' in breakfast:
    coffeeChoice = input('Attendant: Would you like cream in your coffee? ')
    if coffeeChoice == 'yes' or coffeeChoice == 'Yes':
        print('\nAttendant: One coffee with cream coming right up')
    else:
        print('\nAttendant: Black coffee it is\n')

print('\nAttendant: I got your order as')
print(*breakfast, sep = "\n")

userReply = input('\nAttendant: Did I miss anything? ')

if userReply == 'yes' or userReply == 'Yes':
    print("\nI think you're lying")
    print("\nThanks! we'll have your order out right away")
else:
    print("\nThanks! we'll have your order out right away")