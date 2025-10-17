for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0]
    for i in range(n):
        dp.append(a[i] + dp[-1])

    ans = -1
    for l in range(1, n+1):
        for r in range(l, n+1):
            ans = max(ans, (dp[r]-dp[l-1]) // (r-l+1))

    print(ans)