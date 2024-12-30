for _ in range(int(input())):
    n, m = map(int, input().split())
    s = list(input())
    ind = list(map(int, input().split()))
    c = list(input())

    ind.sort(reverse=True)
    c.sort(reverse=True)

    ind = sorted(list(set(ind)), reverse=True)
    l = len(ind)
    c = c[-l:]
    # print(c)

    for i in range(l):
        s[ind[i]-1] = c[i]

    print(''.join(s))
