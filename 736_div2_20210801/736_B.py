from sys import stdin
input = stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    enemy = list(input().rstrip())
    Gregor = list(input().rstrip())
    ans = 0
    for i in range(n):
        if Gregor[i] == '1':
            if enemy[i] == '1' or enemy[i] is None:
                if i > 0 and enemy[i-1] == '1':
                    ans += 1
                elif i < n-1 and enemy[i+1] == '1':
                    ans += 1
                    enemy[i+1] = None
            elif enemy[i] == '0':
                ans += 1
    print(ans)



'''
10
1001011111
1111111111
'''