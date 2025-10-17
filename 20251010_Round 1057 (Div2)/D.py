for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    A = max(a)
    if A >= sum(a) - A:
        print(ans)
        continue

    s = set()
    for ai in a:
        if ai in s:
            s.remove(ai)
            ans += ai * 2
        else:
            s.add(ai)

    if ans == 0:
        print(ans)
        continue

    remains = sorted(list(s))
    if remains:
        ans += remains.pop()
    if remains:
        ans += remains.pop()

    print(ans)