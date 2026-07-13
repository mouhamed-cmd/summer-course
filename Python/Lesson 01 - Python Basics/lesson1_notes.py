name= input ("What is your name?")
fav_number= input ("What is your favorite number?")
asterisks=30
print('*' * asterisks) # print the header line

greeting = 'Hello, ' + name.strip().title() + '!' # clean up the user's name a little bit
white_space_length = (30 - len(greeting) - 3) # how many spaces do we need?
print('* ' + greeting + ' ' * white_space_length + '*')

fav_number = 'Your favorite number is ' + fav_number
print('* ' + fav_number + '  *')
print('*' * asterisks) # print the last header line