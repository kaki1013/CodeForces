# left_append if input < deque[0] else right_append
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    ans = deque([p[0]])
    for i in range(1, n):
        num = p[i]
        if num < ans[0]:
            ans.appendleft(num)
        else:
            ans.append(num)

    print(*ans)
