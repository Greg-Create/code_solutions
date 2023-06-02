#Solution for 16 BIT S/W ONLY

N = int(input())

new = []



for _ in range(N):
    number = input()
    new.append(number)



for i in range(len(new)):
    z = new[i].split(' ')
    for y in range(len(z)):
        z[y] = int(z[y])
   
    if z[-1] == z[0] * z[1]:
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")