for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    count = dict()
    for ai in a:
        if ai in count:
            count[ai] += 1
        else:
            count[ai] = 1
    numbers = sorted(list(count.keys()))

    ans = -1
    for i in range(len(numbers)-1):
        n1, n2 = numbers[i], numbers[i+1]
        c1, c2 = count[n1], count[n2]
        if n1 + 1 == n2:
            # combi n1 & n2
            for big in range(min(c2, m//n2)+1):
                tmp = m - n2 * big
                small = min(c1, tmp//n1)
                tmp = n2 * big + n1 * small
                if tmp <= m:
                    ans = max(ans, tmp)
        else:
            # only n1
            nums = min(c1, m//n1)
            ans = max(ans, n1 * nums)

    # only last
    n1 = numbers[-1]
    c1 = count[n1]
    nums = min(c1, m//n1)
    ans = max(ans, n1 * nums)

    print(ans)
