import sys
import math
all_data = ["2 100 3 30", '100', '50', '50']


integers = [int(x) for x in (all_data[0].split(" "))]


alpacas = [int(x) for x in all_data[1:-1]]

otherSpeeds = [integers[1]/int(x) for x in alpacas]
mySpeed = integers[1]/int(all_data[-1])


count = 0


if all_data[-1] and int(all_data[-1]) > 0:
    zero = False

    for i in alpacas:
        if i == 0:
            zero = True
    if (zero == False):
       

        if all_data[-1] and int(all_data[-1]) >= 0:

            for i in range(len(otherSpeeds)):
                while otherSpeeds[i] <= mySpeed:
                    alpacas[i] = (alpacas[i]*((100-integers[-1]) / 100))
                    otherSpeeds[i] = integers[1]/alpacas[i]
                    count += 1
        if count <= integers[-2]:
            print("YES")
        else:
            print("NO")

    else:
        print("NO")


else:
    print("YES")
