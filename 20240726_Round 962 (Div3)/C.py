"""
arr[idx][26] := int(string[idx]==alphabet[idx])
dp[idx][26] := from start, the number of 등장횟수
    dp[idx-1][26] + arr[idx][26]
"""
oa = ord('a')
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(input())
    b = list(input())

    dp1 = [[0]*26]
    dp2 = [[0]*26]
    for idx in range(n):
        tmp1 = dp1[-1][:]
        tmp2 = dp2[-1][:]

        tmp1[ord(a[idx])-oa] += 1
        tmp2[ord(b[idx])-oa] += 1

        dp1.append(tmp1)
        dp2.append(tmp2)

    # process
    for __ in range(q):
        l, r = map(int, input().split())

        count1 = [dp1[l-1][i] - dp1[r][i] for i in range(26)]
        count2 = [dp2[l-1][i] - dp2[r][i] for i in range(26)]

        ans = sum([abs(count1[i] - count2[i]) for i in range(26)]) // 2

        print(ans)
