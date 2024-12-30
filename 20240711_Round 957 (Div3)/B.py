# 2 = -1 (mod 3) : doesn't affect sum(modulo 3) of row/column
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input())) for _ in range(n)]
    b = [list(map(int, input())) for _ in range(n)]

    diff = [[(a[i][j]-b[i][j]) % 3 for j in range(m)] for i in range(n)]
    diff_t = [[diff[i][j] for i in range(n)] for j in range(m)]

    flag = True
    for i in range(n):
        if sum(diff[i]) % 3 != 0:
            flag = False

    for j in range(m):
        if sum(diff_t[j]) % 3 != 0:
            flag = False

    print('YES' if flag else 'NO')
