for _ in range(int(input())):
    n = int(input())
    s = input()

    if '1' in s:
        print(s.count('1'))
        print(*[i+1 for i in range(n) if s[i] == '1'])
    else:
        print(0)
        print()
