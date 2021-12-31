t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = [s[0]]
    for i in range(1, n):
        if ans[-1] > s[i]:
            ans.append(s[i])
        elif ans[-1] == s[i]:
            if i >= 2:
                if ans[-1] <= ans[-2]:   # zyxxs
                    ans.append(s[i])
                else:
                    break
            else:   # i < 2 : aa
                break
        else:
            break
    ans += ans[::-1]
    print(''.join(ans))