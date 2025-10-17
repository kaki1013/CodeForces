# interactive
import sys


def res(cmd, l, r):
    print(f"{cmd} {l} {r}")
    sys.stdout.flush()
    response = int(input())
    return response


for _ in range(int(input())):
    n = int(input())  # 길이 n

    r_minus_l_plus_1 = res(2, 1, n) - (n * (n+1) // 2)  # res = r - l + 1

    l, r = -1, -1  # ans
    ll, rr = 1, n  # binary search

    while ll != rr:
        m = (ll + rr) // 2
        r1 = res(1, 1, m)
        r2 = res(2, 1, m)

        if r2 - r1 < r_minus_l_plus_1:
            ll = m + 1
        else:  # should be same
            rr = m

    m = (ll + rr) // 2
    r = m
    l = r + 1 - r_minus_l_plus_1
    print(f"! {l} {r}")
    sys.stdout.flush()
