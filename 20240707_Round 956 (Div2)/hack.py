t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    n = [int(i) for i in input().split()]
    r = 1
    s = set()
    for j in n:
        if j in s:
            r += 1
            s = set()
        a = set()
        for w in s:
            if w % j == 0:
                a.add(w // j)
        s = s | a
        if x % j == 0:
            s.add(x // j)
    print(r)
