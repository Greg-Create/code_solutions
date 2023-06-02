import sys
all_data = sys.stdin.read().split('\n')


line = all_data[0].split(" ")


N=int(line[0])
D=int(line[1])
K=int(line[2])
X=int(line[3])

alpacaTimes = []
count = 0
modifiedTimes = []
times = []
zero = True

for i in range(0,len(line)):
    line[i] = int(line[i])
    

    
for i in range(len(all_data)):
    if i != 0:
        if not all_data[i]:
             times.append(0)
        else:
            times.append(int(all_data[i]))
            
if times.count(0) >1:
    print("NO")
    zero=False

if zero:
    if times[-1] == 0:
        print("YES")
        zero = False
   
if zero: 
    for i in times:
        time = D/i
        alpacaTimes.append(time)


    for i in alpacaTimes[:-1]:
        x = K*(i*((100-X)/100))
        modifiedTimes.append(x)

    for i in modifiedTimes:
        if i < times[-1]:
            count += 1

    if count<0:
        print("YES")
        zero = False
    else:
        print("NO")
        zero =False