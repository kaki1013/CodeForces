def when_determine(game_list):  # input := game score list with no '?'
    a, b = 0, 0
    for i in range(10):
        if i == 9:  # 1111111111
            return i + 1
        if game_list[i] == '1':
            if i % 2 == 0:
                a += 1
            else:
                b += 1
        a_rem, b_rem = (9-i)//2, (10-i)//2
        if a > b + b_rem or a + a_rem < b:
            return i + 1  # i-th game = game_list[i] + 1


def how_many_game(string):
    a_list, b_list = [], []  # a win, b win
    for i in range(10):
        if string[i] == '?':
            if i % 2 == 0:
                a_list.append('1')
                b_list.append('0')
            if i % 2 == 1:
                a_list.append('0')
                b_list.append('1')
        else:
            a_list.append(string[i])
            b_list.append(string[i])
    return min(when_determine(a_list), when_determine(b_list))


t = int(input())
for _ in range(t):
    s = list(input())
    print(how_many_game(s))
