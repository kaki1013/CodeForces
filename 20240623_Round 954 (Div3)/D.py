def is_num(c):
    return ord('0') <= ord(c) <= ord('9')


for _ in range(int(input())):
    n = int(input())
    s = list(input())
    m = 9 * 20 + 1  # 9+9+...+9 : min when worst input
    for i in range(n - 1):  # i-th : +/* pass
        for case in range(1 << (n - 2)):  # 0 : +, 1 : *
            op_count = 0
            tmp = [s[0]]
            for j in range(2 * n - 2):
                if j % 2 == 0:  # +, *
                    if j//2 == i:
                        continue
                    if case & (1 << op_count):
                        tmp.append('*')
                    else:
                        tmp.append('+')
                    op_count += 1
                else:  # num
                    idx = (j + 1) // 2
                    c = s[idx]
                    if tmp[-1] == '0':
                        tmp.pop()
                    tmp.append(s[idx])
            # print(tmp)
            res = eval(''.join(tmp))
            m = min(m, res)
    print(m)
