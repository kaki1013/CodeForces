t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if max(a) <= 0 :
        print(n)
    else:
        a = list(set(a))
        a.sort()
        pop_count = 0
        keeper = True
        while keeper:
            for i in range(len(a) - 1 - pop_count):
                if abs(a[i+1] - a[i]) < a[-1-pop_count]:
                    pop_count += 1
            keeper = False
        print(len(a) - pop_count)
