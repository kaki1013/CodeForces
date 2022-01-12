n, l, k = map(int, input().split())
D = list(map(int, input().split()))
A = list(map(int, input().split()))

diff = [D[i+1]-D[i] for i in range(n-1)]
diff.append(l-D[-1])
dp = D + [l]
ans = sum([diff[i] * A[i] for i in range(n)])

removed = [False] * n
count = 0
while count != k:
    # initialize
    first = 0
    for i in range(1, n):
        if not removed[i]:
            second = i
            break
    cut = (A[first] - A[second]) * (dp[second+1] - dp[second])
    cut_pos = second

    # loop
    check = second + 1
    while check < n:
        first = second
        while check < n:
            if not removed[check]:
                second = check
                break
            check += 1
        if cut > (A[first] - A[second]) * (dp[second + 1] - dp[second]):
            cut = (A[first] - A[second]) * (dp[second + 1] - dp[second])
            cut_pos = second
        check += 1

    ans += cut
    removed[cut_pos] = True
    count += 1

print(ans)
