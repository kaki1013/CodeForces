from bisect import bisect_left


def is_possible(arr):
    return 2 * max(arr) < sum(arr)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 3:
        if is_possible(a):
            print(sum(a) if len(set(a)) == 2 else 0)
        else:
            print(0)
        continue

    # n >= 4
    edges = []
    s = set()
    for ai in a:
        if ai in s:
            s.remove(ai)
            edges.append(ai)
            edges.append(ai)
        else:
            s.add(ai)

    edges.sort()
    remains = sorted(list(s))

    if len(edges) == 0:
        print(0)
        continue

    if len(edges) == 2:  # len(remains) >= 2
        edges.append(remains[0])
        edges.append(remains[1])
        if is_possible(edges):
            ans = sum(edges)
            edges.pop()
            edges.pop()

            tmp = sum(edges)
            for i in range(len(remains)):
                e = remains[i]

                edges.append(e)
                if is_possible(edges):
                    ans = max(ans, tmp + e)
                edges.pop()

                idx = bisect_left(remains, tmp + e - 1)  # less than sum of other edges
                if idx == len(remains):
                    idx = len(remains) - 1
                if idx == i:
                    idx -= 1
                if idx < 0:
                    continue

                edges.append(e)
                edges.append(remains[idx])
                if is_possible(edges):
                    ans = max(ans, sum(edges))
                edges.pop()
                edges.pop()

            print(ans)
            continue

        else:
            edges.pop()
            if is_possible(edges):
                print(sum(edges))
            else:
                print(0)
            continue

    # len(edges) >= 4 : at least nonzero(possible)
    if len(remains) == 0:
        print(sum(edges))
        continue

    if len(remains) == 1:
        edges.append(remains[0])
        if is_possible(edges):
            print(sum(edges))
        else:
            edges.pop()
            print(sum(edges))

    # len(remains) >= 2:
    ans = sum(edges)

    tmp = sum(edges)
    for i in range(len(remains)):
        e = remains[i]

        edges.append(e)
        if is_possible(edges):
            ans = max(ans, tmp + e)
        edges.pop()

        idx = bisect_left(remains, tmp + e - 1)  # less than sum of other edges
        if idx == len(remains):
            idx = len(remains) - 1
        if idx == i:
            idx -= 1
        if idx < 0:
            continue

        edges.append(e)
        edges.append(remains[idx])
        if is_possible(edges):
            ans = max(ans, sum(edges))
        edges.pop()
        edges.pop()

    print(ans)