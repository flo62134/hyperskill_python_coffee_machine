# put your python code here
a = int(input())
b = int(input())

total = 0
count = 0

for number in range(a, b + 1):
    if number % 3 == 0:
        total += number
        count += 1

print(total / count)
