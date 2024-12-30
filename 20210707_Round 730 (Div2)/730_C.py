import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    c, m, p, v = map(float, sys.stdin.readline().rstrip().split())
    q = [[c, m, p, v, '', 1]]
    q = deque(q)
    visited = set()
    expected = 0
    while q:
        print(q, expected)
        c, m, p, v, curr, prob = q.popleft()
        if curr + 'c' not in visited and c != 0:
            visited.add(curr + 'c')
            prob = round(prob * c, 7)
            if c > v:
                c, m, p = round(c - v, 7), round(m + v/2, 7), round(p + v/2, 7)
            else:
                c, m, p = 0, round(m + v/2, 7), round(p + v/2, 7)
            if c + m + p <= 1.1:
                q.append([c, m, p, v, curr + 'c', prob])
#            print('c', [c, m, p, v, curr+'c', prob])
        if curr + 'm' not in visited and m != 0:
            visited.add(curr + 'm')
            prob = round(prob * m, 7)
            if m > v:
                c, m, p = round(c + v / 2, 7), round(m - v, 7), round(p + v / 2, 7)
            else:
                c, m, p = round(c + v / 2, 7), 0, round(p + v / 2, 7)
            if c + m + p <= 1.1:
                q.append([c, m, p, v, curr + 'm', prob])
#            print('m', [c, m, p, v, curr+'m', prob])
        if curr + 'p' not in visited and p != 0:
            visited.add(curr + 'p')
            prob = round(prob * p, 7)
            expected = round(expected + (len(curr) + 1) * prob, 7)
    print(expected)