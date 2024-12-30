t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [0] + list(map(int, list(input()))) + [0]
    for t in range(m//2):
        arr.append(0)
        for i in range(n):
            if arr[(n+2)*t + (i+1)] == 1:
                arr.append(1)
            elif arr[(n+2)*t + i] + arr[(n+2)*t + (i+2)] == 1:
                arr.append(1)
            else:
                arr.append(0)
        arr.append(0)

    next_arr = [0]
    for i in range(n):
        if arr[(n + 2) * (m//2) + (i + 1)] == 1:
            next_arr.append(1)
        elif arr[(n + 2) * (m//2) + i] + arr[(n + 2) * (m//2) + (i + 2)] == 1:
            next_arr.append(1)
        else:
            next_arr.append(0)
    next_arr.append(0)

    for t in range(m - m//2 - 1):
        next_arr.append(0)
        for i in range(n):
            if next_arr[(n + 2) * t + (i + 1)] == 1:
                next_arr.append(1)
            elif next_arr[(n + 2) * t + i] + next_arr[(n + 2) * t + (i + 2)] == 1:
                next_arr.append(1)
            else:
                next_arr.append(0)
        next_arr.append(0)

    for i in range(-n-1, -2):
        print(next_arr[i], end='')
    print(next_arr[-2])