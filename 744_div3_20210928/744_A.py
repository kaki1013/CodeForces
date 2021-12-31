t = int(input())
for _ in range(t):
    s = input()
    a, b, c = s.count('A'), s.count('B'), s.count('C')
    print('Yes' if a-b+c==0 else 'No')
