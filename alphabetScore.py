
import sys
alphabet = ["a","b","c","d","e","f","g","h","i","j",'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

score = 0

ar = sys.stdin.read().split('\n')

for i in ar[0]:
    score = score + (alphabet.index(i)+1)

print(score)


