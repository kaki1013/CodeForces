from math import gcd


def min_range(arr, l):
    a = ''.join(arr).split('0')
    temp = [len(cut) for cut in a]
    candidate = [(temp[0] + temp[1] + 1)//2]
    for num in temp[1:]:
        candidate.append((num+1)//2)
    return max(candidate)


t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = input().split()
    ans = -1
    if '0' in a:
        ans = 0
        g = gcd(n, d)
        check = [[a[idx] for idx in range(i, n, g)] for i in range(g)]

        possible = True
        for i in range(g):
            if '0' not in check[i]:
                possible = False
                break

        if possible:
            ans_list = []
            for i in range(g):
                ans_list.append(min_range(check[i], n//g))
            ans = min(ans_list)

    print(ans)
