N = int(input())

lists = []

for _ in range(N):
    x = input()
    lists.append(x)

lists = [i.split(" ") for i in lists]
newList = {}
newarr=[]

for i in range(len(lists)):
    R = int(lists[i][1])
    S = int(lists[i][2])
    D = int(lists[i][3])
    score = (2*R + 3*S +D)
    newList[lists[i][0]] = score

for w in sorted(newList, key=newList.get, reverse=True):
    newarr.append([w, newList[w]])

print()
print(newarr[0][0])
print(newarr[1][0])