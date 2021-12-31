import sys


def isBeautiful(num, k_digits):
    return len(set(list(str(num)))) <= k_digits


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    while not isBeautiful(n, k):
        n += 1
    print(n)

