x = ["1","100","100","53","49"]

for i in range(len(x)):
    x[i] = int(x[i])

del x[0]



n = x[0]
a = x[1]

b=x[2]

c=x[3]


def find_three_numbers(N, A, B, C):
    for i in range(min(A, N) + 1):
        for j in range(min(B, N - i) + 1):
            k = N - i - j
            if k <= C:
                return i, j, k
    return None

# Example usage

result = find_three_numbers(n, a, b, c)
if result is not None:
    print("Numbers found:", result)
else:
    print("No valid combination found.")