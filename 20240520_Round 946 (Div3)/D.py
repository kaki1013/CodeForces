d = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

for _ in range(int(input())):
    n = int(input())
    s = input()

    tmp = (0, 0)
    for i in range(n):
        inst = d[s[i]]
        tmp = (tmp[0]+inst[0], tmp[1]+inst[1])

    if tmp[0] % 2 or tmp[1] % 2:
        print('NO')
        continue

    if n == 2 and tmp[0] == 0 and tmp[1] == 0:
        print('NO')
        continue

    goal = (tmp[0]//2, tmp[1]//2)
    # print(goal)
    check = [False] * n
    if goal[0] > 0:
        count = 0
        for i in range(n):
            if count == goal[0]:
                break
            if s[i] == 'E':
                check[i] = True
                count += 1
    elif goal[0] < 0:
        count = 0
        for i in range(n):
            if count == -goal[0]:
                break
            if s[i] == 'W':
                check[i] = True
                count += 1

    if goal[1] > 0:
        count = 0
        for i in range(n):
            if count == goal[1]:
                break
            if s[i] == 'N':
                check[i] = True
                count += 1
    elif goal[1] < 0:
        count = 0
        for i in range(n):
            if count == -goal[1]:
                break
            if s[i] == 'S':
                check[i] = True
                count += 1

    is_all_false = True
    for i in range(n):
        if check[i]:
            is_all_false = False
    if is_all_false:
        check[0] = True
        goal = d[s[0]]
        goal = (-goal[0], -goal[1])
        if goal[0] > 0:
            count = 0
            for i in range(n):
                if count == goal[0]:
                    break
                if s[i] == 'E':
                    check[i] = True
                    count += 1
        elif goal[0] < 0:
            count = 0
            for i in range(n):
                if count == -goal[0]:
                    break
                if s[i] == 'W':
                    check[i] = True
                    count += 1

        if goal[1] > 0:
            count = 0
            for i in range(n):
                if count == goal[1]:
                    break
                if s[i] == 'N':
                    check[i] = True
                    count += 1
        elif goal[1] < 0:
            count = 0
            for i in range(n):
                if count == -goal[1]:
                    break
                if s[i] == 'S':
                    check[i] = True
                    count += 1
    print(''.join(['R' if check[i] else 'H' for i in range(n)]))
