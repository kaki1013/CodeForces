"""
a + b + c <= x
ab + bc + ca <= n

fixed a.
b + c <= x - a
bc + a(b+c) + a^2 <= n + a^2
    -> (b+a)(c+a) <= n + a^2

0 <= c <= x - a - b
0 <= c <= (n + a^2)/(b+a) - a


when p := b + c, q := bc
p <= x, q + ap <= n

"""

for _ in range(int(input())):
    n, x = map(int, input().split())

    ans = 0
    for a in range(1, x-1):
        upper_bound = int((n+a**2)**0.5)-a
        # print(a, upper_bound)
        for b in range(1, upper_bound + 1):
            if a + b == x:
                continue
            count = min(x - a - b, int((n+a**2)/(b+a))-a)
            if count >= 1:  # c = 1, ..., count
                if count > upper_bound:
                    ans += count + (count - upper_bound)
                else:
                    ans += count
                # print(a, b, count)
    print(ans)