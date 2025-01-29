"""
a_l, ..., a_r 까지 차례대로 먹음
1. k 증가
2. x 이하면 ㄱㅊ, x 초과면 0이 되고 계속 함

a_t를 먹었을 때
(1) x 이하 : 상관 없음
(2) x 초과 : a_t+1이 x 이하면 더 먹음
                    초과면 a_t+2를 살펴봄
==================
dp[i] := sum(a_1, ..., a_i)

a_i에 대해
1. sum(a_i, ..., a_j) <= x이고, sum(a_i, ..., a_j+1) > x인 곳을 찾음
    <=> dp[j] <= dp[i-1] + x이고, dp[j+1] > dp[i-1] + x
    : a_j까지 먹으면 해당 값, a_j+1까지 먹으면 0이 됨
    : a_j+1 먹으면, a_j+2부터 1을 반복함

1 2 1 ? 3 ?
1 2 -> 2
2 1 -> 2
1 -> 1

3 -> 1 + (세그먼트의 첫 원소라면 앞의 원소 개수만큼 추가) 1*4
=====
dp[i] := i에서 끝나는 세그먼트의 수
dp[i] =

ans = sum(dp)

"""
# editorial : https://codeforces.com/blog/entry/131666
from bisect import bisect_left, bisect_right

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    new_a = []
    for i in range(n):
        ai = a[i]
        if ai <= x:
            if new_a == [] or new_a[-1] == []:
                new_a.append([ai])
            else:
                new_a[-1].append(ai)
        else:
            new_a.append([10**9])
    print(new_a)

    dp = []
    for segment in new_a:
        if segment == []:
            dp.append([0])
            continue
        tmp = [0]
        for ai in segment:
            tmp.append(tmp[-1]+ai)
        dp.append(tmp)
    # print(dp)

    ans = 0
    a_idx = -1
    for segment_idx in range(len(new_a)):
        segment = new_a[segment_idx]
        for i in range(len(segment)):
            a_idx += 1
            if new_a[segment_idx][i] == 10**9:
                continue

            j = bisect_left(dp[segment_idx], dp[segment_idx][i] + x) - 1
            j = j - 1 if j == len(segment) else j

            ans += j-i+1
            if i == 0:
                print(segment_idx, i)
                ans += a_idx
            print(segment_idx, i, j, ans)

    print(ans)