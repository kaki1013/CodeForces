for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    d = dict()
    for i in range(n):
        tmp = a[i] % k
        if tmp in d:
            d[tmp].append(a[i])
        else:
            d[tmp] = [a[i]]

    count = -int(n%2==1)
    for key in d.keys():
        count += int(len(d[key]) % 2 == 1)
    if count != 0:
        print(-1)
        continue

    ans = 0
    for key in d.keys():
        tmp = sorted(d[key])
        if len(tmp) % 2 == 0:
            for idx in range(len(tmp)//2):
                l, r = 2*idx, 2*idx+1
                ans += (tmp[r]-tmp[l])//k
        else:
            length = len(tmp)
            left = [tmp[2*length+1]-tmp[2*length] for j in range((length-1)//2)]
            right = [tmp[2*length+2]-tmp[2*length+1] for j in range((length-1)//2)]
            length 