t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [0] + list(map(int, list(input()))) + [0]
    for t in range(m):
        arr.append(0)
        for i in range(n):
            if arr[(n+2)*t + (i+1)] == 1:
                arr.append(1)
            elif arr[(n+2)*t + i] + arr[(n+2)*t + (i+2)] == 1:
                arr.append(1)
            else:
                arr.append(0)
        arr.append(0)
    for i in range(-n-1, -2):
        print(arr[i], end='')
    print(arr[-2])