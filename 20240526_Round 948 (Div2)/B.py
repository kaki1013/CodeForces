def f(arr):
    l = len(arr)
    for i in range(l-1):
        if arr[i] * arr[i+1] != 0:
            return False
    return True


t = int(input())
for _ in range(t):
    x = int(input())
    # x = _ + 1
    b = list(map(int, list(bin(x)[2:])))

    while not f(b):
        b = [0] + b  # 111.. -> 0111..

        # 0 1 1 .. 1 0-> 1 0 0 .. -1
        idx = []  # idx of 11...1

        length = len(b)
        l, r = -1, -1
        for i in range(length-1):
            if b[i] == 0 and b[i+1] == 1:
                l = i+1
                continue
            if l != i and b[i] == 1:  # double 1's
                if b[i+1] == 0:
                    r = i
                    idx.append((l, r))
                    l, r = -1, -1
                    continue
            if l != -1 and i+1 == length-1 and b[i+1] == 1:
                r = i+1
                idx.append((l, r))
                l, r = -1, -1

        for l, r in idx:
            b[l-1] = 1
            for j in range(l, r):
                b[j] = 0
            b[r] = -1

        for i in range(length-1):
            if b[i] == -1 and b[i+1] == 1:
                b[i] = 0
                b[i+1] = -1

    # print out
    b = b[::-1]
    while b[-1] == 0:
        b.pop()

    # ans = 0
    # l = len(b)
    # for i in range(l):
    #     ans += b[i] * 2**i
    # if x != ans or not f(b):
    #     print(x)

    # print([0] + list(map(int, list(bin(x)[2:]))))
    # print(idx)

    print(len(b))
    print(*b)

    # print()
