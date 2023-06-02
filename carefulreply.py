N = int(input())


for _ in range(N):
    x = input()
    z = x.count("<3")
    for i in range(z+1):
        print("<3", end=" ")

    print("")