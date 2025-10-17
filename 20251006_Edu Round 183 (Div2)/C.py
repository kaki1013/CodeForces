# 틀림..
from bisect import bisect_left, bisect_right

for _ in range(int(input())):
    n = int(input())
    s = input()

    # n = 206
    # s = 'a' * 102 + 'b' * 100 + 'a' * 3 + 'b'

    # n = 10
    # s = 'a' * 3 + 'b' * 6 + 'a'

    dp = [(0, 0)]  # (sum, num)
    for i in range(n):
        if s[i] == 'a':
            dp.append((dp[-1][0] + 1, i+1))
        else:
            dp.append((dp[-1][0] - 1, i+1))

    diff = abs(dp[-1][0])

    if diff == 0:
        print(0)
        continue

    # dp = dp[1:]
    dp.sort()
    # print(diff, dp)
    ans = 10**9
    for i in range(n):
        sum_, num = dp[i]

        idx = bisect_right(dp, (sum_ + diff, ))
        # print(i, idx)

        if idx == n + 1:
            continue

        if num == 0 and dp[idx][1] == n:
            continue

        if dp[idx][0] == sum_ + diff:
            ans = min(ans, abs(dp[idx][1] - dp[i][1]))
            # print(111, i, ans)

    if ans == 10**9:
        ans = -1
    print(ans)
