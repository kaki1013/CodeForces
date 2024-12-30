# 실패
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    triples = [(arr[i], arr[i+1], arr[i+2]) for i in range(n-2)]

    d1, d2, d3 = dict(), dict(), dict()
    for tri in triples:
        a, b, c = tri

        if (a, b) in d1:
            d1[(a, b)].append(c)
        else:
            d1[(a, b)] = [c]

        if (b, c) in d2:
            d2[(b, c)].append(a)
        else:
            d2[(b, c)] = [a]

        if (c, a) in d3:
            d3[(c, a)].append(b)
        else:
            d3[(c, a)] = [b]

    ans = 0
    for k1 in d1.keys():
        l = len(d1[k1])
        ans += l*(l-1)//2

    for k2 in d2.keys():
        l = len(d2[k2])
        ans += l*(l-1)//2

    for k3 in d3.keys():
        l = len(d3[k3])
        ans += l*(l-1)//2
    print(d1, d2, d3)
