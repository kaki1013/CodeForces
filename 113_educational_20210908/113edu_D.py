"""
가로선 위에 있는 점들끼리, 혹은 세로선 위에 있는 점들끼리만 보면 됨
(가로선 위와 세로선 위에 있는 점은 반드시 교차점이 생기고 그 점을 지나며 맨하튼 거리와 일치하는 최단경로가 존재함)
(이러한 이유로 가로 도로와 세로 도로의 교차점 위에 있는 도시는 체크할 필요 없음)

서로 다른 가로선 위에 있는 두 점 A와 B에 대해
두 점 사이에 세로선이 존재하면 카운트하지 않고, 존재하지 않으면 카운트 함

세로선에 대해서도 같은 작업을 수행
"""
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    vertical = list(map(int, input().split()))
    horizontal = list(map(int, input().split()))
    v_set = set(vertical)
    h_set = set(horizontal)
    people = [list(map(int, input().split())) for _ in range(k)]
    identifier = [0 for _ in range(k)]  # v : 1, h : 2, both : 3
    for i in range(k):
        person = people[i]
        if person in v_set:
            people[i] += 1
        if person in h_set:
            people[i] += 2
    v_people = [i for i in range(k) if identifier[i] == 1]
    h_people = [i for i in range(k) if identifier[i] == 2]

