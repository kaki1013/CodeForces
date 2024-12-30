from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().rstrip().split())
    if k % 2 == 1:
        if m == 2 and n != 2:
            print('YES')
        else:
            print('NO')
    else:
        if n % 2 == 1 and m % 2 == 0:
            print("No")
        else:
            print("YES")

#
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    if n % 2 == m % 2 == 0:
        if k % 2:
            print("NO")
        else:
            print("YES")
    else:
        tot = k * 2
        if n % 2:
            re = k - m // 2
            if re >= 0 and re % 2 == 0:
                print("YES")
            else:
                print("NO")
        else:
            if k % 2 == 0 and 2 * k <= n * (m - 1):
                print("YES")
            else:
                print("NO")
