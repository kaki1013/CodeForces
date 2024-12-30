# https://codeforces.com/contest/1995/submission/272157814
# https://codeforces.com/contest/1995/submission/272144293
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    if 1 in a:
        for i in range(n):
            if a[n-1-i] == 1:
                last_one = n-1-i
        for i in range(last_one):
            if a[i] != 1:
                ans = -1
                break
        if ans == -1:
            print(ans)
            continue
    for i in range(1, n):
        while a[i] < a[i-1]:
            a[i] = a[i]**2
            ans += 1

    print(ans)
