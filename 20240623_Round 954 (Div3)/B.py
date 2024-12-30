for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            tmp = -1
            neigh = 0
            bigger = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii = i + dx
                jj = j + dy
                if 0 <= ii < n and 0 <= jj < m:
                    neigh += 1
                    if a[i][j] > a[ii][jj]:
                        bigger += 1
                        tmp = max(tmp, a[ii][jj])

            if neigh == bigger:
                a[i][j] = tmp

    for line in a:
        print(*line)
