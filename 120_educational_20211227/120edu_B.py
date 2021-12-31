# 참고: https://codeforces.com/contest/1622/submission/140823464
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n

    s = input()
    liked, disliked = [], []
    for i in range(n):
        song = i + 1
        if s[i] == '1':
            liked.append((p[i], i))
        else:
            disliked.append((p[i], i))
    liked.sort()
    disliked.sort()

    for i in range(len(disliked)):
        q[disliked[i][1]] = i + 1
    for i in range(len(liked)):
        q[liked[i][1]] = len(disliked) + i + 1

    print(*q)