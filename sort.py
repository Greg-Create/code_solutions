N = int(input())

numbers = []

for _ in range(N):
    number = int(input())
    numbers.append(number)

numbers.sort()


for i in numbers:
    print (i)