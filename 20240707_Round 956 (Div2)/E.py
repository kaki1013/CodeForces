"""
1 <= n <= 10^2
1 <= a <= 10^4
1 <= b <= min(10^4, an)
-> 0 <= na-b <= 10^6-1
na-b는 1자리~6자리 수

n이 l자리(l = 1,2,3) 수라면
an-b는 al-b 길이

1 <= al-b <= 6 이므로
al-6 <= b <= al-1
"""
for _ in range(int(input())):
    s = input()
    l = len(s)
    n = int(s)

    ans = 0
    ans_list = []

    for a in range(1, 10000+1):
        for b in range(a*l-6, a*l):
            tmp = a*s
            if len(tmp) > b and n*a-b == int(tmp[:-b] if b else tmp):  # b=0이면 오류 : b<=1은 그냥 넘겨도 됐을 듯
                if 1 <= b <= min(10000, a*n):
                    ans += 1
                    ans_list.append((a, b))

    print(ans)
    for a, b in ans_list:
        print(a, b)