x = input().split(" ")

for i in range(len(x)):
    x[i] = int(x[i])
    

if (x[0] < x[1]) and (x[2]<x[3]):
    print("Go to the department store")
elif (x[0] < x[1]) and x[2]>=x[3]:
    print("Go to the grocery store")
elif(x[2]<x[3]) and x[0]>=x[1]:
    print("Go to the pharmacy")
else:
    print("Stay home")
