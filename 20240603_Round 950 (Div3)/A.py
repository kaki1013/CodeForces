for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()

    d = dict()
    for c in a:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    ans = 0
    for c in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        if c not in d:
            ans += m
            continue
        count = d[c]
        if count < m:
           ans += m-count
    print(ans)
