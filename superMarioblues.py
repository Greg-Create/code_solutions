N = int(input())

for _ in range(N):
    x = [int(i) for i in input().split('-') ]

    points = 0
    for i in range(x[0], 8):
        if(x[1] == 4):
            x[0] +=1
        x[1] +=1

 
    points = 0
    if(x[0] == 1):
        for i in range(x[1],4):
            points += 1
            if i == 2:
                x[0] = 4
                x[1] =1
                break
    if(x[0] == 4):
        for i in range(x[1],4):
            points += 1
            if i == 2:
                x[0] = 8
                x[1] =1
                break

    if(x[0]>1 and x[0]<4):
        temp = ((4-x[0] +1) * 4) - x[1] +1
    

   
                
    

    points = points + ((8-x[0] +1) * 4) - x[1] +1
    print(points)