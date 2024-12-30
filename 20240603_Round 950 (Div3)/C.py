for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = int(input())
    d = list(map(int, input().split()))

    star = set()
    need = dict()
    for i in range(n):
        if a[i] == b[i]:
            star.add(a[i])
        else:
            bi = b[i]
            if bi in need:
                need[bi] += 1
            else:
                need[bi] = 1

    max_i = -1
    for i in range(m-1, -1, -1):
        if d[i] in star:
            max_i = i

    flag = True
    for i in range(max(0, max_i), m):
        di = d[i]
        if di in need:
            if need[di] > 0:
                need[di] -= 1
        else:
            flag = False
            break

    ddd = dict()
    for i in range(m if max_i == -1 else max_i):
        pass


    for k in need.keys():
        count = need[k]
        if count > 0:
            pass
        elif count == 0:
            pass  # do nothing
        else:
            pass  # impossible



    # dd = dict()
    # for di in d:
    #     if di in dd:
    #         dd[di] += 1
    #     else:
    #         dd[di] = 1
    #
    # remain = set()
    # for i in range(n):
    #     bi = b[i]
    #     if a[i] == b[i]:
    #         remain.add(bi)
    #     else:
    #         if bi in dd:
    #             dd[bi] -= 1
    #         else:
    #             dd[bi] = -1
    #
    # max_last = 0  # we can ignore the operations before this,
    # for idx in range(n-1, -1, -1):
    #     if b[idx] in remain:
    #         max_last = idx
    #         break
    #
    # flag = True
    #
    # for idx in range(m):
    #
    #
    # for k in dd.keys():
    #     if dd[k] < 0:
    #         print(1, k)
    #         flag = False
    #         break
    #     if (dd[k] > 0) and (k not in remain):
    #         print(2, k, (dd[k] > 0) , (k not in remain))
    #         flag = False
    #         break
    # print(dd)
    # print(remain)
    # print(flag)