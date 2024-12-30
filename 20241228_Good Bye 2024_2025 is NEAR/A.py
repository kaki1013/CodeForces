def is_stable(arr):
    if len(arr) == 1:
        return True
    if len(arr) == 2:
        a, b = min(arr), max(arr)
        return 2*a > b
    for i in range(n-1):
        if is_stable(arr[i:i+2]):
            # print(arr[i:i+2])
            return True
    return False


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print('YES' if is_stable(arr) else 'NO')
