N = int(input())

inputs = []

for _ in range(N):
    inputs.append(input())



for i in range(len(inputs)):
    inputs[i] = inputs[i].split(" ",1)

for i in inputs:
    y=int(i[0])
    x = i[1]
    mispelled = x[:y-1] + x[y:]
    print(inputs.index(i) + 1, mispelled)