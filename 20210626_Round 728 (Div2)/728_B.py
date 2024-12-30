t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    arr = [2 * n + 1] + list(map(int, input().split()))

    for N in range(3, 2 * n):
        i= (N - 1) // 2
        j = N - i
        while True:
            if i >= j:
                break
            if arr[i] * arr[j] == i + j:
                answer += 1
                print(i, j)
            i += 1
            j -= 1
    print(answer)