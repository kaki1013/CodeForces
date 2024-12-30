from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1 or n == 2:
        print(2 ** n - 1)
        continue
    ans = n + n * (n - 1) // 2 + n * (n - 1) * (n - 2) // 6
    print(ans)  # 3이상 모름
