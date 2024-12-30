for _ in range(int(input())):
    a, b, c = map(int, input().split())

    ans = -1
    for i in range(6):  # 0~5
        for j in range(6-i):  # 0~5-i
            k = 5-i-j
            tmp = (a+i)*(b+j)*(c+k)
            ans = max(ans, tmp)
    print(ans)
