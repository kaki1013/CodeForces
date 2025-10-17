for _ in range(int(input())):
    a, b = map(int, input().split())
    aa, bb = map(lambda x:bin(x)[2:], [a, b])
    la, lb = len(aa), len(bb)
    if len(aa) >= len(bb):
        print(2)
        first = (a ^ b) & ~(1 << (la-1))
        second = a ^ b ^ first
        print(first, second)
    else:
        print(-1)
