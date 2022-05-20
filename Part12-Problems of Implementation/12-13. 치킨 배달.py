#입력 구간
N, M = map(int, input().split())
city = []
for i in range(N):
    row = list(map(int, input().split()))
    city.append(row)

#1. 집 위치, 치킨집 위치를 좌표로 저장하기
house = []
chicken = []
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            house.append([r,c])
        if city[r][c] == 2:
            chicken.append([r,c])

#2. 치킨 거리 계산하기
distance = []
distanceList = []
for r1c1 in house:
    for r2c2 in chicken:
        d = abs(r1c1[0] - r2c2[0]) + abs(r1c1[1] - r2c2[1])
        distance.append(d)
    distanceList.append(distance)
    distance = []

#3. 치킨집을 임의로 M개 뽑았을 때, 그때의 치킨 거리
from itertools import combinations
chickenList = list(range(len(chicken)))
_chicken = list(combinations(chickenList, M))
__distanceList = []
result = []
resultList = []

for __chicken in _chicken:
    for _distanceList in distanceList:
        for i in __chicken:
            __distanceList.append(_distanceList[i])
        result.append(min(__distanceList))
        __distanceList = []
    resultList.append(sum(result))
    result = []
print(min(resultList))
                


