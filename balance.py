N = int(input())
numbers = list(map(int, input().split()))

total_sum = sum(numbers)
dp = [[False] * (total_sum + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(total_sum + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
        if j >= numbers[i - 1] and dp[i - 1][j - numbers[i - 1]]:
            dp[i][j] = True

min_diff = total_sum
for j in range(total_sum // 2, -1, -1):
    if dp[N][j]:
        min_diff = total_sum - 2 * j
        break

print(min_diff)