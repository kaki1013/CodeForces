"""
1. 지지 않음(이기거나 무승부) / 2. 한번이라도 이김

전체적으로 = 로 초기화하고 (i,i)는 X로 수정
이 경우 1의 조건을 모두 만족하며, 1은 더 이상 건드릴 필요가 없음.
2를 위해 1을 건드릴 경우 1에게 패배가 생기고, 1에게 굳이 승리를 만들어주면 불필요한 패배가 생김(패배는 요건에 없으므로 없는게 이득)

따라서 '2'들만 신경쓰면 되는데, 기본적인 규칙은 다음과 같음
1. (i,j)가 +면 (j,i)는 -
2. (가능한 경우라면) 2번을 기대한 사람들이 a, b, c라고 하면 a가 b를, b가 c를, c가 a를 이기도록 수정

가능한 경우는?
2번을 선택한 사람이 m명이면 고려해야할 게임의 수는 mC2 = m(m-1)//2 이고
m(m-1)//2 >= m 을 만족해야 하므로 m = 0 또는 m >= 3
"""

t = int(input())
for _ in range(t):
    n = int(input())
    expectations = list(map(int, list(input())))
    twos = expectations.count(2)
    board = [['=' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        board[i][i] = 'X'
    if twos == 0:
        print('Yes')
        for line in board:
            print(''.join(line))
    elif twos >= 3:
        print('Yes')
        twos_idx = [i for i in range(n) if expectations[i] == 2]
        l = len(twos_idx)
        twos_idx.append(twos_idx[0])
        for i in range(l):
            win, lose = twos_idx[i], twos_idx[i+1]
            board[win][lose] = '+'
            board[lose][win] = '-'
        for line in board:
            print(''.join(line))
    else:
        print('NO')
