lists = ['Fr','qp','HH','db','  ' ,'pq']

new=[]

for i in lists:
    if i == "  ":
        break
    else:
        new.append(i)



for i in range(len(new)):
    new[i] = list(new[i])

print("Ready")
for i in new:
    if ((i[0] == 'q' and i[1]=='p') or (i[0] == 'p' and i[1]=='q')):
        print("Mirrored pair")
    elif ((i[0] == 'd' and i[1]=='b') or (i[0] == 'b' and i[1]=='d')):
        print("Mirrored pair")
    else:
        print("Ordinary pair")