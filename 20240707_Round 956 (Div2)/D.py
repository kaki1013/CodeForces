from collections import deque

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = 'L' + input() + 'L'

    vst = [False] * (n+2)
    start, finish = 0, n+1
    q = deque([(start, k)])
    vst[start] = True
    reachable = False
    while not reachable and q:
        curr, remain = q.popleft()

        if a[curr] == 'L':
            for jump in range(1, m+1):
                nxt = curr+jump
                if nxt <= n+1 and (not vst[nxt]) and a[nxt] != 'C':
                    if nxt == finish:
                        reachable = True
                        break
                    q.append((nxt, remain))
                    vst[nxt] = True
        elif a[curr] == 'W':
            nxt = curr + 1
            if nxt <= n+1 and (not vst[nxt]) and a[nxt] != 'C' and remain > 0:
                if nxt == finish:
                    reachable = True
                    break
                q.append((nxt, remain-1))
                vst[nxt] = True

    print('YES' if reachable else 'NO')
