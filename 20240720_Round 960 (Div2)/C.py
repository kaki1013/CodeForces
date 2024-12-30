"""
1 1 2 2 3 3 4 4

한번 구해지고 나면 계속 밀림: 이전 까지는 substring이라서 MAD값이 무조건 유지되고 결국 한칸씩 밀림
0 1 1 2 2 3 3 4
0 0 1 1 2 2 3 3
0 0 0 1 1 2 2 3
0 0 0 0 1 1 2 2
0 0 0 0 0 1 1 2

b는 단조 증가(강한 X)
0 0 1 1 1 1 1 2 3 3 4 4 5
-> 0:2, 1:5, 2:1, 3:2, 4:2, 5:1
0 0 0 1 1 1 1 1 1 3 3 4 4
(1) if value=1, move prev -> 0:2, 1:6, 3:2, 4:3
(2) -1 (not key=0) -> 0:2, 1:5, 3:1, 4:2
(3) +1 (not largest) -> 0:3, 1:6, 3:2, 4:2
0 0 0 0 1 1 1 1 1 1 3 3 4
(1) if value=1, move prev -> 0:3, 1:6, 3:2, 4:2
(2) -1 (not key=0) -> 0:3, 1:5, 3:1, 4:1
(3) +1 (not largest) -> 0:4, 1:6, 3:2, 4:1
0 0 0 0 0 1 1 1 1 1 1 1 4
0 0 0 0 0 0 1 1 1 1 1 1 1
...


"""
def is_all_zero(arr):
    for a in arr:
        if a:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = sum(a)

    # construct b
    count = [0] * (n+1)
    b = []
    for i in range(n):
        ai = a[i]
        count[ai] += 1
        if count[ai] >= 2:
            b.append(max(b[-1], ai))
        else:
            if b:
                b.append(b[-1])
            else:
                b.append(0)
    """
    0 0 0 0 1 1 1 1 1 1 3 3 4
    (1) if value=1, move prev -> 0:3, 1:6, 3:2, 4:2
    (2) -1 (not key=0) -> 0:3, 1:5, 3:1, 4:1
    (3) +1 (not largest) -> 0:4, 1:6, 3:2, 4:1
    """

    if len(set(b)) != 1:  # b has something, not zero
        # count b
        for i in range(n):
            if b[i] != 0:
                key = b[i]
                value = 1
                idx = i
                break

        stack = []
        for i in range(idx+1, n):
            if key == b[i]:
                value += 1
            else:
                stack.append([key, value])
                key = b[i]
                value = 1
        stack.append([key, value])

        for key, value in stack:
            ans += key * value

        while stack:
            new_stack = []
            for k, v in stack:
                if v == 1:
                    if new_stack:
                        new_stack[-1][1] += 1
                else:
                    new_stack.append([k, v])
            if new_stack:
                new_stack[-1][1] -= 1
                for k, v in new_stack:
                    ans += k * v
            stack = new_stack

        print(ans)
    else:
        print(ans)