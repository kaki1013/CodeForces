"""
xor from 1 to n (https://www.geeksforgeeks.org/calculate-xor-1-n/)
Method 2 (Efficient method) :
1- Find the remainder of n by moduling it with 4.
2- If rem = 0, then xor will be same as n.
3- If rem = 1, then xor will be 1.
4- If rem = 2, then xor will be n+1.
5- If rem = 3 ,then xor will be 0.
"""
import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    r = (a - 1) % 4

    x = 0
    if r == 0:
        x = a - 1
    elif r == 1:
        x = 1
    elif r == 2:
        x = a

    ans = a
    if x != b:
        x ^= b
        if x in range(a):
            ans += 1
        else:
            if x == a:
                ans += 2
            else:
                ans += 1
    print(ans)
