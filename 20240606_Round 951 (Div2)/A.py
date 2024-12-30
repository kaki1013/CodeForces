for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    tmp = min([max(a[i], a[i+1]) for i in range(n-1)])-1
    print(tmp)