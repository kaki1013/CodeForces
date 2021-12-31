t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = []
    for i in range(n):
        char = s[i]
        if char == 'U':
            ans.append('D')
        elif char == 'D':
            ans.append('U')
        else:
            ans.append(char)
    print(''.join(ans))
