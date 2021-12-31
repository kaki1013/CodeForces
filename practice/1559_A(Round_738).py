t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = a[0]
    for i in range(1, n):
        m &= a[i]
    print(m)