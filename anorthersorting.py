z = input()

x = [int(i) for i in input().split(" ")]

newlist =[]

for i in x:
   y = [int(z) for z in list(str(i))]
   newlist.append(y)


z = sorted(newlist, key=lambda x: x[1] )


last = z[-1]
for i in range(len(z)):
   current = i
   for x in range(i+1,len(z)):
      if(z[current][1] == z[x][1]):
         if(z[current][0] < z[x][0]):
            current = x
            (z[i], z[current]) = (z[current], z[i])



finalList = []
for i in z:
    y = [str(x) for x in i]
    finalList.append(''.join(y))

strin = ""

for i in finalList:
   strin += i+" "

print(strin.strip())
