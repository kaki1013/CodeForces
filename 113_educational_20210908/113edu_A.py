t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = [-1, -1]
    found = False
    for i in range(n):
        if found:
            break
        for j in range(i):
            string = s[j:i+1]
            if string.count('a') == string.count('b'):
                ans = [j+1, i+1]
                found = True
                break
    print(*ans)