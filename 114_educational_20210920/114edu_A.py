t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, n+1):
        arr = ['(' for _ in range(i)]
        for __ in range(i):
            arr.append(')')
        for __ in range(n-i):
            arr.append('(')
            arr.append(')')
        print(''.join(arr))


