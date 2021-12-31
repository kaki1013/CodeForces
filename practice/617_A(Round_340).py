# https://codeforces.com/problemset/problem/617/A
n = int(input())
if n%5 == 0:
    r = 0
else:
    r = 1
print(n//5 + r)