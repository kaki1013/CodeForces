# 실패
"""
1. Dye a 2×2 subgrid white;
2. Dye a whole row white. Note you can "not" dye a whole column white.
By operation 2, we can make a goal in n step.

We should use operation 1, if a_i and a_(i+1) is either 0, 1, or 2.
If a = (1,1,1), we have two options
    1. (1,1) & 1
    2. 1 & (1, 1)
So we can choose "greedy"

2 4 4 2 -> (1, 2) + (3, 4) + (2, 3) : 3 step
2 4 6 8 8 6 4 2 -> (1, 2) + (3, 4) + (5, 6) + (7, 8) + (2, 3) + (4, 5) + (6, 7) + (3, 4) + (5, 6) + (4, 5) : 10 step

# greedy - remove all rows with >4 b cells. Then keep 2 flags whether you used the first 2 or last 2 in the previous row
"""
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # print(0, 0, a)

    ans = 0
    for i in range(n):
        if a[i] > 4:
            a[i] = 0
            ans += 1
    # print(1, ans, a)

    for i in range(n - 1):
        if 0 < a[i] <= 2 and 0 < a[i + 1] <= 2:
            a[i] = 0
            a[i + 1] = 0
            ans += 1
    # print(2, ans, a)

    for i in range(n - 3):
        a1, a2, a3, a4 = a[i:i + 4]
        if 0 < a1 <= 2 and 0 < a2 <= 4 and 0 < a3 <= 4 and 0 < a4 <= 2:
            a[i] = 0
            a[i + 1] = 0
            a[i + 2] = 0
            a[i + 3] = 0
            ans += 3
    # print(3, ans, a)

    for i in range(n):
        if a[i]:
            a[i] = 0
            ans += 1
    # print(4, ans, a)

    print(ans)
"""
반례
1
10
2 0 1 4 4 4 4 2 0 1
"""