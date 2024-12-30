# max_heap: (remain, index)
# if remain == 0: don't push
# len(max_heap) == 0 or 1: finish
import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans, ans_list = 0, []
    q = []
    for i in range(n):
        if a[i] == 0:
            continue
        idx = i + 1
        heapq.heappush(q, [-a[i], idx])

    while True:
        if len(q) in [0, 1]:
            break
        x, y = heapq.heappop(q), heapq.heappop(q)
        x[0] += 1
        y[0] += 1
        ans += 1
        ans_list.append((x[1], y[1]))
        if x[0]:
            heapq.heappush(q, x)
        if y[0]:
            heapq.heappush(q, y)

    print(ans)
    for answer in ans_list:
        print(*answer)
