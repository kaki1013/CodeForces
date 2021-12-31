t = int(input())
for _ in range(t):
    n, m, r, c, x, y = map(int, input().split())
    temp = [x - r if r <= x else 2 * n - x - r, y - c if c <= y else 2 * m - y - c]
    print(min(temp))
