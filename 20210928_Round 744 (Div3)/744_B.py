t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)

    ans, ans_list = 0, []
    for i in range(n):
        if a[i] == a_sorted[i]:
            continue
        left, right = i+1, n
        for m in range(i+1, n):
            if a[m] == a_sorted[i]:
                move = m - i
                break
        a = a[:i] + a[i+move:n] + a[i:i+move]
        ans += 1
        ans_list.append((left, right, move))
    print(ans)
    for answer in ans_list:
        print(*answer)
