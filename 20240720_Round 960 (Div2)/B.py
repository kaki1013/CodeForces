"""
array b의 길이 = m
maximum prefix position = x
b_1 + ... + b_x 가 최대
b_(x+1) + ... + b_m <= 0

maximum suffix position = y
b_y + ... + b_m 이 최대
b_1 + ... + b_(y-1) <= 0

1 <= y < x <= n

1,.., y-1, y, .., x, x+1, .., n
?, .., -1, y, .., x, -1, .., n
"""

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    ans = [1] * n

    for i in range(y-1, 0, -1):  # y-1, ..., 1
        idx = (y-1) - i  # y-1, ..., 1 -> 0, 1, ..
        if idx % 2 == 0:
            ans[i-1] = -1

    for i in range(x+1, n+1):  # x+1, ..., n
        idx = i - (x+1)
        if idx % 2 == 0:
            ans[i-1] = -1

    print(*ans)
