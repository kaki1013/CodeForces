for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    aa, bb = 0, 0
    minus, plus = 0, 0
    for i in range(n):
        if a[i] > b[i]:
            aa += a[i]
        elif a[i] < b[i]:
            bb += b[i]
        elif a[i] == 1:
            plus += 1
        elif a[i] == -1:
            minus += 1

    if aa < bb:
        aa, bb = bb, aa
    # aa >= bb

    diff = aa - bb
    tmp = min(diff, minus)
    aa -= tmp
    minus -= tmp
    # aa >= bb

    if minus:
        aa -= minus//2
        bb -= minus//2
        if minus % 2:
            bb -= 1

    diff = aa - bb
    tmp = min(diff, plus)
    bb += tmp
    plus -= tmp
    # aa >= bb

    if plus:
        aa += plus//2
        bb += plus//2
        if plus % 2:
            bb += 1

    print(min(aa, bb))
