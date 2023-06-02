#SOlution of AN Animal Contest 2 P1 Koala Konundrum

N = int(input())
Z = input()
X = list(Z)
D = set(X)
odd= 0
even=0
for i in D:
    if Z.count(i)%2==0:
        even+=1
    else:
        odd+=1
print(max(1,odd))