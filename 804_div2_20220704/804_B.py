pat1, pat2 = [], []
for i in range(25):
    if i % 2:
        pat1.append(1)
        pat1.append(0)
        pat2.append(0)
        pat2.append(1)
    else:
        pat1.append(0)
        pat1.append(1)
        pat2.append(1)
        pat2.append(0)
ans = []
for i in range(25):
    if i % 2:
        ans.append(pat1)
        ans.append(pat2)
    else:
        ans.append(pat2)
        ans.append(pat1)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    for i in range(n):
            print(*ans[i][:m])