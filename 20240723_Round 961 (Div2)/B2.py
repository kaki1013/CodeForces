"""
1
2 10000000000
11 12
87312315 753297050

WA
87312315 753296985
9999999285

ANS
87312309 753297050
9999999999
"""
for _ in range(int(input())):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    count = dict()
    for i in range(n):
        count[A[i]] = C[i]
    numbers = sorted(list(count.keys()))

    ans = -1
    for i in range(len(numbers)-1):
        n1, n2 = numbers[i], numbers[i+1]
        c1, c2 = count[n1], count[n2]
        if n1 + 1 == n2:
            # combi n1 & n2
            tmp = min(c1+c2, m//n1)
            # diff = m - n1 * tmp

            x2 = m - n1 * tmp
            # x1 = (m-n2*x2)//n1

            x1 = tmp - x2  # x1 > c1 : possible
            # print(x1, x2, x1+x2, n1*x1+n2*x2)
            #
            x1 = min(x1, c1)
            x2 = min(x2, tmp - x1)
            # print(x1, x2, x1+x2, n1*x1+n2*x2)


            # x1 = min(c1, tmp)
            # x2 = tmp - x1
            # print(n1, n2, x1, x2)
            tmp = n1*x1+n2*x2
            if ans < tmp <= m:
                print(n1, n2, x1, x2, x1+x2, tmp)
                ans = tmp

            # for big in range(min(c2, m//n2)+1):
            #     tmp = m - n2 * big
            #     small = min(c1, tmp//n1)
            #     tmp = n2 * big + n1 * small
            #     if tmp <= m:
            #         ans = max(ans, tmp)
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

print(87312309, 753297050, 87312309 + 753297050)