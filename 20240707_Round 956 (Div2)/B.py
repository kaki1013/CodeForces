for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for aa in a:
        if aa == 1:
            ans += 1
        else:
            ans += 2*aa-1

    M = max(a)
    ans -= 2*M-1

    print(ans)
