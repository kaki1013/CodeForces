t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    if n % 2 == 0:
        for i in range(n // 2):
            arr.append(2 * i + 2)
            arr.append(2 * i + 1)
        for i in range(n - 1):
            print(arr[i], end=' ')
        print(arr[-1])
    elif n == 3:
        print(3, 1, 2)
    else:
        print(3, 1, 2, end=' ')
        arr = []
        for i in range((n - 3) // 2):
            arr.append(2 * i + 5)
            arr.append(2 * i + 4)
        for i in range(n - 4):
            print(arr[i], end=' ')
        print(arr[-1])