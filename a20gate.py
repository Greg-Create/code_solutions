N = int(input())

new = []

for _ in range(N):
    new.append(int(input()))


for i in new:
    stop = False
    while stop == False:
        i+=1
        x = i**3
        if x%1000 == 888:
            print(i)
            stop=True

