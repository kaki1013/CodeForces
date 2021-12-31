t = int(input())
for _ in range(t):
    n = int(input())
    cut = []
    for i in range(n):
        l, r = map(int, input().split())
        cut.append((r-l, l, r))
    cut.sort()

    chosen = [False] * (n + 1)
    for i in range(n):
        __, l, r = cut[i]
        candidate = []
        for j in range(l, r+1):
            if not chosen[j]:
                d = j
                chosen[d] = True
                break
        print(l, r, d)