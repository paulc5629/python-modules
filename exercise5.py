#exercise 5 Task 1
'''
number_guess = int(input("Guess the number?"))
magic_number=21

if number_guess == magic_number:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the correct number is {magic_number}.")
'''

#exercise 5 Task 2
'''
guest_age = int(input("Guest's age?"))

if guest_age<2 :
    print("Hello, baby")
elif guest_age>2 and guest_age<4 :
    print("Hello, toddler")
elif guest_age>4 and guest_age<13 :
    print("Hello, Kiddo")
elif guest_age>13 and guest_age<20:
    print("Hello, Teenager")
elif guest_age>20 and guest_age<65:
    print("Hello, Adult")
elif guest_age>45:
    print("Hello, Elderly")
'''

#exercise 5 Task 3
'''
fav_fruits = ['Apple', 'Pears', 'Plums']

for fruit in fav_fruits:
    if fruit == "Apple":
        print("I like apples too!")
    elif fruit == "Pears":
        print("I like pears too!")
    elif fruit == "Plums":
        print("I like plums too!")
    elif fruit == "Bannas":
        print("I don't like bananas!")
    else:
        print("I don't know what that fruit is.")
'''

#exercise 5 Task 4
'''
user_list = ['Enya', 'paul', 'James', 'Admin', 'Snowball']

if not user_list:
    print("The list is empty.")
else:
    for user in user_list:
        if user == 'Admin':
            print("Access granted to Admin user")
        else:
            print(f"Welcome back {user}")
'''

#exercise 5 Task 5
'''
exist_user = ['Enya', 'Scott', 'Pete', 'Frank', 'Paul']
new_user = ['Enya', 'paul', 'James', 'Pat', 'Snowball']

for user in new_user:
    user.upper()
    if user in exist_user:
        print(f"{user} already exists in the database.")
    else:
        print(f"{user} has been added to the database.")
'''