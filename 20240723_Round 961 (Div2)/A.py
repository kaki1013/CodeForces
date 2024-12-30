"""
1 2 3
4 5 6
7 8 9

3 2 2 1 1
"""

for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = 0
    if k:
        tmp = min(k, n)
        k -= tmp
        ans += 1
    for i in range(2*(n-1)):
        if k == 0:
            break
        length = (n-1) - i//2

        tmp = min(length, k)
        k -= tmp
        ans += 1

    print(ans)
