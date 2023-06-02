N = [int(x) for x in input().split(" ")]

cheese = []
coupon = 0
total = 0 


for _ in range(N[0]):
    x = input()
    lists = [int(i) for i in x.split(" ")]
    cheese.append(lists)


for i in cheese:
   total = total +i[0]

for i in range(N[1]+1):
    total = total-cheese[i][0]+cheese[i][1]

print(total)