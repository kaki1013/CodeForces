for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    ans = list('+' * n)

    l, r = s.count('0'), s.count('1')
    u = k - l - r  # unknown?

    for i in range(l):
        ans[i] = '-'
    for i in range(r):
        ans[-i-1] = '-'
    for i in range(u):
        ans[l+i] = '?'
        ans[-r - 1 - i] = '?'

    if k == n:
        ans = '-' * n

    print(''.join(ans))
