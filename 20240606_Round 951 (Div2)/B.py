for _ in range(int(input())):
    x, y = map(int, input().split())
    z = x^y

    tmp = 0
    while z % 2 == 0:
        z //= 2
        tmp += 1
    print(2**tmp)
