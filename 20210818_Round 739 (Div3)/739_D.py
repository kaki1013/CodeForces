"""
# 10**9-> delete 9(all zeros), 9 digit number -> delete 9(all) + add 1('1') = 10 times, max = 10
# initial: original_length + 1(all delete + add '1')
import sys
from collections import deque


def isPowerOfTwo(x):  # x is string
    x = int(x)
    if x == (x&-x):
        return True
    return False


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = sys.stdin.readline().rstrip()
    made = set()
    q = deque([(n, 0)])
    while q:
        now, count = q.popleft()
        if now in made:
            continue
        if now == '':
            count += 1
            break
        elif now[0] == '0':
            q.append((now[1:], count + 1))
            continue
        if isPowerOfTwo(now):
            print('break', now, count)
            break
        for i in range(len(now)):
            candidate = now[:i]+now[i+1:]
            if candidate not in made:
                q.append((candidate, count+1))
                made.add(now)
        for i in range(10):
            candidate = now + str(i)
            if candidate not in made:
                q.append((candidate, count+1))
                made.add(now)
    print(count)
"""
# 10**9-> delete 9(all zeros), 9 digit number -> delete 9(all) + add 1('1') = 10 times, max = 10
# initial: original_length + 1(all delete + add '1')
import sys


def isPowerOfTwo(x):  # x is string
    x = int(x)
    if x == (x & -x):
        return True
    return False


def common(num, power_two):  # parameters are strings  //  num은 단조이면 퐁당퐁당도 가능
    l1, l2 = len(num), len(power_two)
    length = 0
    for check_len in range(1, l2+1):
        if check_len > l1:
            break
        for start in range(l1-check_len+1):
            if power_two[:check_len] == num[start:start+check_len]:
                length = max(length, check_len)
    return length


arr = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192', '16384', '32768',
       '65536', '131072', '262144', '524288', '1048576', '2097152', '4194304', '8388608', '16777216', '33554432',
       '67108864', '134217728', '268435456', '536870912', '1073741824', '2147483648', '4294967296', '8589934592']
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = sys.stdin.readline().rstrip()
    l = len(n)
    ans = l + 1
    for power in arr:
        ans = min(ans, l + len(power) - 2 * common(n, power))
    print(ans)