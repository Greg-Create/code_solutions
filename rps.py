N = int(input())


for _ in range(N):
    x = input()
    if(x=="Scissors"):
        print("Rock")
    elif(x=="Fox"):
        print("Foxen")
    elif(x=="Paper"):
        print("Scissors")
    elif(x=="Rock"):
        print("Paper")
    else:
        break