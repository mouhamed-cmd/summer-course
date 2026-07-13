# number = float(input("Give me one number "))
# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negatif")
# else:
#     print("zero") CTRL +? COMMENT EVERYTHING

# number = int(input("Enter the number"))
# if number > 0:
#     print ("The number is positive")
# else:
#     print ("the number is not positive")

# number = int(input("Enter a number:"))
# if number %2 ==0:
#     print("the number is odd")
# else:
#     print("the number is even")

# age = int(input("How old are you?"))
# if age < 13:
#     print("Child")
# elif age >=13 and age <=19:
#     print("Teenager")
# elif age >=20 and age <=64:
#     print("Adult")
# else:
#     print("Senior")

# for number in range(1,11):
#     print (number)

# my_name_list=["Bob","Jack","Ryan"]
# my_name_list.append("Michael")
# my_name_list.append("Chris")
# print(my_name_list)

# for name in my_name_list:
#     print(name)

number=int(input("Enter a even integer number"))
while number % 2 == 1:
    number=int(input("Enter a even integer number"))

print(f"Good job! You entered an even number, {number}")


secret_number=22

user_guess = int(input("Guess an integer number: "))
count=1

while user_guess != secret_number:
    if user_guess < secret_number:
        print("Your guess was too low!")
    else:
        print("Your guess was too hight!")
    user_guess = int(input("Guess an integer number: "))
    count+=1

print(f"Congratulations, you gueesed the correct number, {user_guess}")
print(f"It took you {count} guesses.")

