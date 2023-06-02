limit = int(input())
speed = int(input())
difference = speed-limit

if(1<=difference<=20):
    print("You are speeding and your fine is $100." )
elif(21<=difference<=30):
    print("You are speeding and your fine is $270." )
elif(31<=difference):
    print("You are speeding and your fine is $500." )
else:
    print("Congratulations, you are within the speed limit!")
