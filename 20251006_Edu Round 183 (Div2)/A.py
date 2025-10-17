for _ in range(int(input())):
    n = int(input())
    if n % 3:
        print(3 - (n % 3))
    else:
        print(0)
