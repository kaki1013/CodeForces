from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    q = n // 3
    if n % 3 == 0:
        print(q, q)
    elif n % 3 == 1:
        print(q+1, q)
    else:
        print(q, q+1)
