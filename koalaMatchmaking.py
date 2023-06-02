N = int(input())

max = int((N+(N-1))/2)


print(max)

for i in range(N):
    x= int((i+N)/2)
    if  x> max:
        max = x
