import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, a, b = map(int, sys.stdin.readline().rstrip().split())
    visited = set()
    q = deque([1])
    m = 1
    s = {1}
    check = False
    while True:
        if n < m or not q:
            print('No')
            break
        elif check:
            print('Yes')
            break
        else:
            m = 10 ** 9 + 1
            x = q.popleft()
            if a*x not in visited and a*x <= n and a != 1:
                visited.add(a*x)
                q.append(a * x)
            elif a * x > n or a == 1:
                if (n-x) % b == 0:
                    print('Yes')
                    break
                else:
                    m = min(m, a * x, x + b)
                    continue
            if x+b not in visited and x+b <= n:
                visited.add(x + b)
                q.append(x+b)
            m = min(m, a * x, x + b)
            if n == a * x or n == x + b:
                check = True