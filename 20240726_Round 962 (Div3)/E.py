"""
# naive
mod = 10 ** 9 + 7
for _ in range(int(input())):
    s = input()
    n = len(s)

    count = 0
    for l in range(n):
        for r in range(l, n):
            for x in range(l, r+1):
                for y in range(x, r+1):
                    tmp = 0
                    for i in range(x, y+1):
                        if s[i] == '1':
                            tmp += 1
                    if tmp*2 == y-x+1:
                        count += 1
    print(count)

01010101
01234567

"0과 1의 개수가 같게 하는 구간 (x, y)에 대해 (x, y)를 포함하는 구간의 개수" 의 합

(x, y)를 포함하는 구간의 개수 = (x - 0 + 1) * ((length-1) - y + 1) = (x+1) * (length - y)


====================
https://codeforces.com/contest/1996/submission/272850433
MOD = 1000000007

def solve():
    s = input().strip()
    n = len(s)

    prefix = [0] * (n + 1)
    count = [0] * (2 * (n + 1))

    for i in range(n):
        prefix[i+1] = prefix[i] + (1 if s[i] == '1' else -1)

    cnt = 0
    for i in range(1, n + 1):
        count[prefix[i-1] + n] += i
        cnt += count[prefix[i] + n] * (n - i + 1)

    print(cnt % MOD)

for _ in range(int(input())):
    solve()

"""

mod = 10 ** 9 + 7
for _ in range(int(input())):
    s = input()
    n = len(s)

    count = 0
    for l in range(n):
        for r in range(l, n):

            tmp = 0
            for i in range(l, r+1):
                if s[i] == '1':
                    tmp += 1
            if tmp*2 == r-l+1:
                count += (l+1)*(n-r)
    print(count % mod)