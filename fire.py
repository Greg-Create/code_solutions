x = [int(i) for i in input().split(" ")]
y = [int(i)for i in input().split(" ")]

y.sort()

for i in range(0,x[1]):
    y[i] = y[i]*2

y.sort()

print(y[0])