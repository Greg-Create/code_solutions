#Solution for AppleBy contest '19 P3 -A Recursion Problem, 
#Find simpler solution in this case brackets didnt matter all you had to do was sum up all the digits 
s = input()
y = s.replace('(','').replace(')','').replace('+','')
lists = y.split(' ')
new = [int(i) for i in lists if i!='']



print(sum(new))
