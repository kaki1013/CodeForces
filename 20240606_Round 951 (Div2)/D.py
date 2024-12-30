def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def check(arr):
    l = len(arr)
    for i in range(l-1):
        if a[i] > a[i+1]:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = [gcd(a[i], a[i+1]) for i in range(n-1)]

    idx = []
    for i in range(n-1-1):
        if b[i] > b[i+1]:
            idx.append((i, i+1))

    if len(idx) > 2:
        print('No')
        continue

    idx_ = []
    for aa, bb in idx:
        if aa not in idx_:
            idx_.append(aa)
        if bb not in idx_:
            idx_.append(bb)

    flag = False
    for i in idx_:
        bb = []
        for j in range(n-1):
            if j+1 == i:
                bb.append(gcd(a[j], a[j+2]))
            else:
                bb.append(gcd(a[j], a[j+1]))
        if not check(bb):
            flag = True
            break
    print('Yes' if flag else 'No')