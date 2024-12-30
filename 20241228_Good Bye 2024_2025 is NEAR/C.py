for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = 0

    l, r = 1, n
    m = (l + r) // 2
    length = r - l + 1
    depth = 0
    old_m = 0
    while length >= k:
        m = (l + r) // 2
        if length % 2:
            if depth:
                ans += m * (2 ** depth) + old_m * (2 ** (depth - 1))
            else:
                ans += m * (2 ** depth)
            r = m - 1
        else:
            r = m
        length //= 2
        depth += 1
        old_m += m

    print(ans)
