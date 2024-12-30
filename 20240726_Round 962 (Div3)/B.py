for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [list(map(int, list(input()))) for _ in range(n)]

    d = n//k
    ans = []
    for i in range(d):
        tmp = []
        for j in range(d):
            # print(k*i, k*j)
            # print(a[k*i][k*j])
            tmp.append(a[k*i][k*j])
        ans.append(tmp[:])
    for line in ans:
        for x in line:
            print(x, end='')
        print()
