# be_hacked
q = int(input())
for _ in range(q):
    s, t = input(), input()
    l_s, l_t = len(s), len(t)
    start = t[0]
    start_idx_list = [i for i in range(l_s) if s[i] == start]
    correct_input = False
    for start_idx in start_idx_list:
        idx, check_idx = start_idx, 0
        while idx+1 < l_s and check_idx+1 < l_t and s[idx] == t[check_idx]:
            if s[idx+1] == t[check_idx+1]:
                idx += 1
                check_idx += 1
            else:
                break
        while idx-1 >= 0 and check_idx+1 < l_t and s[idx] == t[check_idx]:
            if s[idx-1] == t[check_idx+1]:
                idx -= 1
                check_idx += 1
            else:
                break
        if l_t-1 == check_idx:
            print("YES")
            correct_input = True
            break
    if not correct_input:
        print("NO")
