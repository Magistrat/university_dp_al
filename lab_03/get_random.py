from random import random


new_list = []
for _ in range(10000):
    new_list.append(random())


with open("random.txt", "w") as file:
    for line in new_list:
        file.write(f'{line}' + '\n')
