lists = [int(input()),int(input()),int(input()),int(input()),int(input())]



def nearestFibonacci(num):
     
    if (num == 0):
        return
 

    first = 0
    second = 1
 
    third = first + second
 

    while (third <= num):
         
        first = second
 
        second = third
 
        third = first + second
 

    if (abs(third - num) >=
        abs(second - num)):
        ans =  second
    else:
        ans = third
    
    return ans

for i in lists:
    print(nearestFibonacci(i))