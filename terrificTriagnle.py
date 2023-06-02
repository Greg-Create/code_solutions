N = int(input())

triangles = []

for _ in range(N):
    x= input().split(" ")
    z = [int(i) for i in x]
    z.sort()
    triangles.append(z)


for i in triangles:
    if((i[0]**2) + (i[1]**2) == (i[2]**2)):
        print("R")
    elif ((i[0]**2) + (i[1]**2)>(i[2]**2)):
        print("A")
    elif ((i[0]**2) + (i[1]**2)<(i[2]**2)):
        print("O")


