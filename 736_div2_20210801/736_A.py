t = int(input())
for _ in range(t):
    P = int(input())
    for i in range(2, P-1):
        if (P-1)%i == 0:
            print(i, P-1)
            break
