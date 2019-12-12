import random

number = []
for i in range(45):
    number.append(i+1)
print(number)

numbers = random.sample(range(1,46),6)
print(numbers)