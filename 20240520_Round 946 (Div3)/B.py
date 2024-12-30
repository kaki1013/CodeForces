for _ in range(int(input())):
    n = int(input())
    b = input()

    tmp = sorted(list(set(b)))
    d = dict()
    l = len(tmp)
    for idx in range(l):
        d[tmp[idx]] = tmp[l-1-idx]
    ans = ''.join([d[b[i]] for i in range(len(b))])
    print(ans)