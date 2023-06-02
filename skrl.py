x = ["1 1", "22 13", "3 3"]
new = []

for i in x:
    new.append(i.split(" "))

for i in new:
    for x in range(len(i)):
         i[x] = int(i[x])

for i in new:
    count = 0

    if(i[0]==1):
        count = count + 1
    if (i[0] == 1 and i[1]<7):
        count = count+1
    if(i[0] <4 and i[1]<4):
        count =count+1
    if(count>0):
        print("bad")
    else:
        print("good")

