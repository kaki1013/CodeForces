import itertools as iter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    success = False
    for arr in iter.permutations(a):
        for i in range(2*n):
            if i != 2*n-1 and 2 * arr[i] == arr[i-1] + arr[i+1]:
                break
            if i == 2*n-1 and 2 * arr[i] == arr[i-1] + arr[0]:
                break
            if i == 2*n-1:
                success = True
        if success:
            print(list(arr))
            break