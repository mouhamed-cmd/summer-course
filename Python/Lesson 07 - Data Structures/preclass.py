signals = []
with open("preclass_problem1_data.txt", 'r') as in_file:
    for line in in_file:
        signal = int(line)
        signals.append(signal)
signals_sorted = sorted(signals, reverse=True)
high_5 = signals_sorted[:5]
coordinate = sum(high_5) / 10.0
print(f"the coordinate is {coordinate}")



# Exercise 3
# Write a function that doubles the elements in a list.

def double_list