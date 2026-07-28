import random

with open('output.txt') as output_file:
    for i in range(100):
        random_number=str(random.randint(1,1000))
        output_file.write(random_number + "\n")

with open('output.txt','r') as input_file:
    lines = input_file.readlines()

new_list =[]
for line in lines:
    line = line.strip()
    line = int(line)






    lines_stripped = [int(line.strip()) for line in lines]
    print(lines_stripped)

min = 1000
max = 0
count = 0
sum = 0


name = "kane"
print(name)

5/0

alpha=int('a','b','c')
print(aplha)