import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    d = abs(a-b)
    if d == 0:
        print(0, 0)
    elif d == 1:
        print(1, 0)
    elif a == 0 or b == 0 or a==d or b==d:
        print(d, 0)
    else:
        print(d, min(abs(a // d * d - a), abs(a // d * d + d - a)))