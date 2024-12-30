"""
s/t
strategy : s[i]에 s[1, ..., n]을 차례대로 xor하므로 짧게 설정하면 원하는 비트만 스위치 가능

s[0]이 0이면, t[0]은 0이어야 함 : 수정이 불가
s[0...l]=0...1(l에서 처음 0)이면 해당 부분은 같아야 함

s에서 처음 1나오기 전까지는 동일해야 함
"""
def is_possible(s, t):
    if '1' not in s:
        if '1' not in t:
            return True
        return False
    first = -1
    n = len(s)
    for i in range(n):
        if s[i] == '1':
            first = i
            break

    for i in range(first):
        if s[i] != t[i]:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()

    print("YES" if is_possible(s, t) else "NO")
