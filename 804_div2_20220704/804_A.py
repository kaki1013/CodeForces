t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2:
        print(-1)
        continue
    a, b, c = n//2, 0, 0
    print(a, b, c)
