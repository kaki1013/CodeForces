import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    count_odd = 0
    for num in arr:
        if num % 2 == 1:
            count_odd += 1
    if count_odd == n:
        print('Yes')
    else:
        print('No')