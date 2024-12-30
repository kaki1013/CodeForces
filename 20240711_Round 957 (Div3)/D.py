"""
r-l = q-p does not matter
lemma.
column(위 아래가 한 묶음)끼리는 바꿀 수 있다. : 자명함

ex.
1 3 4 2 5
7 1 2 5 4
에서
3과 2, 7과 4를 바꾸고자 함
1) column끼리 교환 :
1 5 4 2 3
7 4 2 5 1
2) a의 2와 3 바꾸고, b의 7과 4를 바꿈 (거리가 1로 동일)
1 5 4 3 2
4 7 2 5 1
3) 1에서 바꾼 위치를 다시 바꿈
1 2 4 3 5
4 1 2 5 7
: 결국 3,2와 4,7이 바뀜
"""

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

