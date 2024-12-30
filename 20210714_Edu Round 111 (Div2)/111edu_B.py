from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    string_list = input().rstrip()
    if b >= 0:
        print((a + b) * n)
    else:  # minimize the number of 'cut'
        change = 0
        for i in range(n-1):
            if string_list[i] != string_list[i+1]:
                change += 1
        b_count = (change + 3) // 2
        print(a * n + b * b_count)
