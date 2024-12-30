t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    if n == len(set(A)):    # 중복되는 원소가 1개라도 있어야 가능
        print(-1)
        continue
    pos = dict()            # 해당 값(key)을 가지는 인덱스를 리스트(value)로 저장할 딕셔너리
    for i in range(n):
        a = A[i]
        if a in pos:
            pos[a].append(i)
        else:
            pos[a] = [i]
    ans = []                # 가능한 정답 후보들
    for p in pos:
        if len(pos[p]) == 1:    # 2개 이상의 원소를 가지는 값들만 체크
            continue
        pos[p].sort()
        min_dist = 10**6
        for j in range(len(pos[p])-1):      # 해당 값에 대해서 가장 가까운 두 원소를 체크: 원소가 가까울수록 더 긴 세그먼트를 채택 가능
            min_dist = min(min_dist, pos[p][j+1]-pos[p][j])
        # 해당 값에 대해서, 조건을 만족하는 subsegment 중 최대 길이 = 왼쪽과 오른쪽 원소 각각으로부터 양 끝까지의 길이의 합 = n - 두 원소 사이의 거리
        ans.append(n - min_dist)
    print(max(ans))                 # 가능한 후보들 중 최대 값