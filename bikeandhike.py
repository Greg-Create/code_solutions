x =[int(x) for x in input().split(" ")]
y = list(input())


speed = x[1]
walk = 0

for i in y:
    print(speed)
    if(speed==0): 
        walk=walk+1
        if(i=='D'):
            speed=speed+1
    else:
        if(i=='U'):
            speed = speed-1
        elif(i=="D"):
            speed=speed+1
        else:
            speed=speed
   
       


print(walk)