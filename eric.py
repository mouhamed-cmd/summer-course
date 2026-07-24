# import random

# random_integer = random.randint(50,100)
# print(random_integer)


# import random

# # File name to store the random numbers
# filename = "random_numbers.txt"

# # Open the file in write mode
# with open(filename, "w") as file:
#     for _ in range(100):
#         number = random.randint(50, 100)  # Generate a random integer between 50 and 100
#         file.write(f"{number}\n")         # Write each number on a new line

# print(f"100 random integers have been written to '{filename}'.")
# random.randint(50, 100) 

# #Open this file, find max, and average

# with open ("random_numbers.txt", "r") as input_file:
#     lines = input_file.readlines()
#     #rint(lines)
#     count = 0
#     min = 1000
#     max = 0
#     sum = 0
#     for line in lines:
#         amount = int(line)
#         sun += amount
#         count+=1
#         if amount > max:
#             max = amount
#         if amount <min:
#             min = amount 
#             average = sum/count
# print(f"Max: {max}, Min: {min}, Average: {average}")

import os
current = os.getcwd
print (current)