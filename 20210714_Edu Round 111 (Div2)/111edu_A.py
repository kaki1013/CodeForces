from collections import deque
from sys import stdin
input = stdin.readline
"""
t = int(input())
for _ in range(t):
    s = int(input())
    q = deque([(1, 1)])  # sum, count
    ans = 5001
    while q:
        sum_arr, count = q.popleft()
        if sum_arr == s:
            ans = min(ans, count)
        if sum_arr+1 <= s:
            q.append((sum_arr + 1, count + 1))
        if sum_arr+2 <= s:
            q.append((sum_arr + 2, count + 1))
    print(ans)
"""
t = int(input())
for _ in range(t):
    s = int(input())
    print(int((s-1)**0.5)+1)
'''
    dp = [0, 1, 2] + [-1] * s
    for i in range(s):
        dp[i+3] = min(dp[i+2], dp[i+1]) + 1
    print(dp)
    print(dp[s])
'''