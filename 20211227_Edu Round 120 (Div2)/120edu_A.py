t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    a, b, c = sorted([a, b, c])
    able = False
    if c == a + b:
        able = True
    else:
        if len({a, b, c}) < 3:
            if (a + b + c) % 2 == 0:
                able = True
    print("YES" if able else "NO")
