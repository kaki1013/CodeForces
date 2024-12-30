t = int(input())
for _ in range(t):
    k = int(input())
    n = int((k-1)**0.5) + 1
    i = k - (n-1)**2
    diff = abs(n**2-n+1-k)
    if k > n**2-n+1:
        print(n, n-diff)
    else:
        print(n-diff, n)
