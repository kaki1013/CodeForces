import math

t = int(input())
for _ in range(t):
    a = int(input())
    while a >= 11:
        k = 1
        while True:
            if math.log10(9 * a + 1) - 1 < k <= math.log10(9 * a + 1):
                break
            k += 1
        a -= int('1' * k)
    if a == 0:
        print('YES')
    else:
        print('NO')