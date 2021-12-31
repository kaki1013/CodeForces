from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))

    count, idx_dict = dict(), dict()
    for i in range(n):
        num = arr[i]
        if num not in count:
            count[num] = 1
            idx_dict[num] = [i]

        else:
            count[num] += 1
            idx_dict[num].append(i)

    ans = [0 for _ in range(n)]

    temp = []
    i = 0
    l = 0  # length of temp
    while i < n:
        if arr[i] not in count:
            i += 1
            continue
        if count[arr[i]] > k:
            count[arr[i]] -= 1
        elif count[arr[i]] == k:
            temp_for_k = 0
            for j in idx_dict[arr[i]]:
                if j < i:
                    continue
                temp_for_k += 1
                ans[j] = temp_for_k
            del count[arr[i]]
        else:
            for j in idx_dict[arr[i]]:
                temp.append(j)
                l += 1
            del count[arr[i]]
        i += 1

    for _ in range(l % k):
        temp.pop()

    i = 0
    for idx in temp:
        ans[idx] = i % k + 1
        i += 1

    print(*ans)