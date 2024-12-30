for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    if n * m == 1:
        print(-1)
    else:
        b = [(a[(i + 1) % n][1:]) + [a[(i + 1) % n][0]] for i in range(n)]
        for line in b:
            print(*line)
