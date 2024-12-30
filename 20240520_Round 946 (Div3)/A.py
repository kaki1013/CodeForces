from math import ceil

for _ in range(int(input())):
    x, y = map(int, input().split())
    ans = ceil(y/2)
    remain = 15*ans - 4*y

    x -= remain
    if x > 0:
        ans += ceil(x/15)

    print(ans)