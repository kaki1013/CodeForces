import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    n = abs(a - b)
    if not (a <= 2 * n and b <= 2 * n and c <= 2 * n):
        print(-1)
    else:
        print(n + c if c <= n else c - n)
