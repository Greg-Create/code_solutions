N = int(input())

lists = []

for _ in range(N):
    x = list(input())
    lists.append(x)
    

for x in lists:
    for i in x:
        if(i=="a" or i=="A"):
            print("Hi!", end=" ")
        if(i=="e" or i=="E"):
            print("Bye!", end=" ")
        if(i=="i" or i=="I"):
            print("How are you?",end=" ")
        if(i=="O" or i=="o"):
            print("Follow me!",end=" ")
        if(i=="U" or i=="u"):
            print("Help!",end=" ")
        if(i.isnumeric()):
            print("Yes!",end=" ")
    print()
            


