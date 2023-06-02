N = int(input())

x = []
z=[]

for _ in range(N*2):
    y = input()
    x.append(y)

for i in range(len(x)):
    if(len(x[i])>1):
        x[i] = x[i].split(" ")
    else:
        x[i] = int(x[i])


for i in x[1::2]:
    for y in range(len(i)):
        i[y] = int(i[y])
    
    i.sort()
    
    print(i[0], " ", i[-1])


