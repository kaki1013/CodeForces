# 실패
from bisect import bisect_right

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    tot = sum(a)
    goal = (tot//3 + 1) if tot % 3 else tot//3

    # dpX[i] := sum of X[0:i]
    dpA = [a[0]]
    for i in range(1, n):
        dpA.append(dpA[-1]+a[i])
    dpB = [b[0]]
    for i in range(1, n):
        dpB.append(dpB[-1]+b[i])
    dpC = [c[0]]
    for i in range(1, n):
        dpC.append(dpC[-1]+c[i])

    # print(dpA)
    # print(dpB)
    # print(dpC)

    flag = False
    idxA, idxB, idxC = -1, -1, -1
    for i in range(n-2):  # [0, i], [i+1, l], [l+1, n-1]
        # A
        if dpA[i] >= goal:
            idxA = 1, i+1
            # B
            l = bisect_right(dpB, dpB[i]+goal)  # [i+1, l]
            if l < n-1 and dpC[-1] - dpC[l] >= goal:
                idxB = i+2, l+1
                idxC = l+2, n
                flag = True
                break
            # C
            l = bisect_right(dpC, dpC[i]+goal)  # [i+1, l]
            if l < n-1 and dpB[-1] - dpB[l] >= goal:
                idxB = l+2, n
                idxC = i+2, l+1
                flag = True
                break

        # B
        if dpB[i] >= goal:
            idxB = 1, i+1
            # A
            l = bisect_right(dpA, dpA[i]+goal)  # [i+1, l]
            if l < n-1 and dpC[-1] - dpC[l] >= goal:
                idxA = i+2, l+1
                idxC = l+2, n
                flag = True
                break
            # C
            l = bisect_right(dpC, dpC[i]+goal)  # [i+1, l]
            if l < n-1 and dpA[-1] - dpA[l] >= goal:
                idxA = l+2, n
                idxC = i+2, l+1
                flag = True
                break

        # C
        if dpC[i] >= goal:
            idxC = 1, i+1
            # A
            l = bisect_right(dpA, dpA[i]+goal)  # [i+1, l]
            if l < n-1 and dpB[-1] - dpB[l] >= goal:
                idxA = i+2, l+1
                idxB = l+2, n
                flag = True
                break
            # B
            l = bisect_right(dpB, dpB[i]+goal)  # [i+1, l]
            if l < n-1 and dpA[-1] - dpA[l] >= goal:
                idxA = l+2, n
                idxB = i+2, l+1
                flag = True
                break

    if flag:
        tmp = []
        for l, r in [idxA, idxB, idxC]:
            tmp.append(l)
            tmp.append(r)
        print(*tmp)
    else:
        print(-1)
