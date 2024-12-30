from math import gcd

def lcm2(a, b):
    return a*b//gcd(a,b)

def lcm(*arr):
    tmp = lcm2(arr[0], arr[1])
    for x in arr[2:]:
        tmp = lcm2(tmp, x)
    return tmp

for _ in range(int(input())):
    n = int(input())
    k = list(map(int, input().split()))

    l = lcm(*k)

    if sum([l // kk for kk in k]) >= l:  # sum([1/kk for kk in k]) > 1:
        print(-1)
        continue

    x = [10 ** 9 // ki for ki in k]

    # cost = sum(x)
    # gain = sum([k[i]*x[i] for i in range(n)])

    print(*x)
