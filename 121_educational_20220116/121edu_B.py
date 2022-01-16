t = int(input())
for _ in range(t):
    x = list(input())
    l = len(x)
    inc = False
    for i in range(l-1):
        if int(x[i]) + int(x[i+1]) >= 10:
            inc = True
            last_idx = i
    if inc:
        for i in range(last_idx):
            print(x[i], end='')
        print(int(x[last_idx])+int(x[last_idx+1]), end='')
        for i in range(last_idx+2, l):
            print(x[i], end='')
        print()
    else:
        print(int(x[0]) + int(x[1]), end='')
        for i in range(2, l):
            print(x[i], end='')
        print()
