# 틀림
# https://codeforces.com/contest/1989/submission/267741351

for _ in range(int(input())):
    a = input()
    b = input()
    l1, l2 = len(a), len(b)

    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                tmp = dp[i][j]
                if a[i-tmp+1:i] == b[j-tmp+1:j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    max_len = max([max(dp[i]) for i in range(len(a)+1)])
    print(l1+l2-max_len)
