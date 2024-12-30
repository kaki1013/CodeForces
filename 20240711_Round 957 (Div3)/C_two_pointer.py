# 성공
def two_pointer(A, B, C, goal):
    n = len(A)

    l, r = 0, 0  # ans : [0, l], [l+1, r], [r+1, n-1]
    while l < n-2 and A[l] < goal:
        l += 1
    while r < n-1 and B[r] - B[l] < goal:
        r += 1
    if l < n-2 and r < n-1 and C[-1] - C[r] >= goal:
        return True, [1, l+1, l+2, r+1, r+2, n]
    return False, -1


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

    dp = [dpA, dpB, dpC]
    ans = -1
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if len({i, j, k}) == 3:
                    tmp = two_pointer(dp[i], dp[j], dp[k], goal)
                    if tmp[0]:
                        ans = [0] * 6

                        ans[2*i] = tmp[1][0]
                        ans[2*i+1] = tmp[1][1]
                        ans[2*j] = tmp[1][2]
                        ans[2*j+1] = tmp[1][3]
                        ans[2*k] = tmp[1][4]
                        ans[2*k+1] = tmp[1][5]

    if ans == -1:
        print(-1)
    else:
        print(*ans)