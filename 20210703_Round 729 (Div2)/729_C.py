import sys


def Not_divisor(n):
    i = 2
    while True:
        if n % i != 0:
            return i
        i += 1


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    ans = 0
    for i in range(1, n+1):
        print(Not_divisor(i))
        ans = (ans + Not_divisor(i)) % (10 ** 9 + 7)
    print(ans)