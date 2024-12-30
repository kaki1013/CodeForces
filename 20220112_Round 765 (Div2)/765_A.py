t = int(input())
for _ in range(t):
    n, l = map(int, input().split())
    x = list(map(int, input().split()))
    count = [0] * l
    for num in x:
        s = bin(num)[2:]
        le = len(s)
        for i in range(-1, -le-1, -1):
            if int(s[i]):
                count[i] += 1
    ans = 0
    for i in range(l):
        if count[i] > n//2:
            ans += 2**(l-1-i)
    print(ans)