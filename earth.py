
boulder = [int(x) for x in input().split(" ")]
coordinates = [int(x) for x in input().split(" ")]


if ((coordinates[0]<boulder[0]<coordinates[2]) and (coordinates[1]<boulder[1]<coordinates[3])):
    print("Yes")
else:
    print("No")