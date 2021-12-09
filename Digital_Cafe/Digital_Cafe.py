#Digital Cafe
import Digital_Cafe_Func as dcf

dcf.cls()

print(f'''{dcf.colors.header}Welcome to the Digital Cafe
---------------------------\n''')

print(f"{dcf.colors.assistant}Hi, my name is Aey-I, I'll be your sever today. What can I get started for you?\n")
print(f'''{dcf.colors.reset}Enter your order below
*NOTE: Please put a comma in between each item\n''')

userBreakfast = input().lower()
breakfast = userBreakfast.split(', ')
#dcf.breakFastOrder(userBreakfast)

breakfast = userBreakfast

dcf.itemStyle(breakfast)

userResponse = input(f'{dcf.colors.assistant}\nAey-I: Can I get anything else for you? ').lower()

#dcf.addToOrder(breakfast, userResponse)
while 'yes' in userResponse:
    extraOrder = input(f'{dcf.colors.assistant}\nAey-I: What would you like? ').lower()
    dcf.itemStyle(extraOrder)
    breakfast.append(extraOrder)
    userResponse = input(f'{dcf.colors.assistant}\nAey-I: Can I get anything else for you? ').lower()
    

print(f'{dcf.colors.assistant}\nAey-I: I got your order as')
print(*breakfast, sep = "\n")

userReply = input(f'{dcf.colors.assistant}\nAey-I: Did I miss anything? ').lower()
if 'yes' in userReply:
    forgottenOrder = input(f'{dcf.colors.assistant}\nAey-I: What did I miss? ').lower()
    dcf.itemStyle(forgottenOrder)
    breakfast.append(forgottenOrder)
    print(f'{dcf.colors.assistant}\nAey-I: Sorry about that, I added {forgottenOrder} to your order')

print(f"{dcf.colors.assistant}\nAey-I: Thanks! we'll have your order out right away")
