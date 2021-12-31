N = int(input())
arr_set = list()
nope = list()
want_print_list = list()

for i in range(2*N):
    if i % 2 == 0:
        nope.append(input())
    if i % 2 == 1:
        arr_set.append(list(map(int, input().split())))
# [[3, 5, 1, 4, 6, 6], [1, 2, 3], [1, 3, 3, 4], [1, 6, 3, 4, 5, 6]]
# length 1 check

for arr in arr_set:
    count = 0
    for s_p in range(len(arr) - 1):
        for dist in range(1, len(arr) - s_p):
            if arr[s_p + dist] - arr[s_p] == dist:
                count += 1
    print(count)

