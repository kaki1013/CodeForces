"""
... 홀
... 홀 짝

"""

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = [0] * (n+1)
    for i in range(n):
        count[a[i]] += 1
    count = [c for c in count if c]
    # print(count)

    flag = False
    for c in count:
        if c % 2 == 1:
            flag = True
            break
    print('YES' if flag else 'NO')
