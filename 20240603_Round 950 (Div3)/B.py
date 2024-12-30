for _ in range(int(input())):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))

    f = a[f-1]
    a.sort(reverse=True)

    if a[k-1] == f:
        if k-1 == n-1:
            print('YES')
            continue
        if a[k] < f:
            print('YES')
        elif a[k] == f:
            print('MAYBE')
    elif a[k-1] > f:  # a[k-1] ... f
        print('NO')
    elif a[k-1] < f:
        print('YES')
