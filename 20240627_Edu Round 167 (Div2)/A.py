for _ in range(int(input())):
    x, y = map(int, input().split())
    # possible = (y-abs(x)+1) >= -x
    print('YES' if y>= -1 else 'NO')
