n = int(input())
arr = list(map(int, input().split()))

dp = [[[0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        dp[i][j] = arr[i] % arr[j]

s = []
for i in range(n):
    temp = 0
    for j in range(i):
        temp += dp[j][i]
    s.append(temp)


t = []
for i in range(n):
    temp = 0
    for j in range(i):
        temp += dp[i][j]
    t.append(temp)

p = [0]
for i in range(n-1):
    p.append(p[i] + s[i+1] + t[i+1])
print(*p)