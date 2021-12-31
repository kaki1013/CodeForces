t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dd = dict()
    ans = 0
    for i in range(n):
        check = abs(a[i])
        if check in dd:
            dd[check] += 1
        else:
            dd[check] = 1
    ss = set([abs(aa) for aa in a])
    for aa in list(ss):
        check = abs(aa)
        if check == 0:
            ans += 1
        else:
            ans += min(dd[check], 2)
    print(ans)