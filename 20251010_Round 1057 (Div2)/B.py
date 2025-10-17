def bin32(n):
    bn = bin(n)[2:]
    bn = '0' * (32-len(bn)) + bn
    return list(map(int, bn))


def solve(x, y, z):
    for i in range(32):
        if x[i] == y[i] == z[i]:
            continue
        if x[i] + y[i] + z[i] == 1:
            continue
        return False
    return True


for _ in range(int(input())):
    x, y, z = map(int, input().split())
    x, y, z = map(bin32, [x, y, z])
    print('YES' if solve(x, y, z) else 'NO')
