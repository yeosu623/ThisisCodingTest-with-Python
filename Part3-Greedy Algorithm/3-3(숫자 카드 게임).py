#3.3 숫자 카드 게임

#입력 조건
print("n m 입력조건은? (1 <= n, m <= 100)")
n, m = map(int, input().split())

#알고리즘 선택
#이 문제는 각각의 경우마다 동일한 규칙을 적용한다. 따라서 탐욕 알고리즘을 쓴다.

#문제 해결 전략
#각각의 행을 선택할 때, 가장 숫자가 낮은 수를 선택하고 저장한다.(output)
#그 다음 행을 선택하고, 가장 숫자가 낮은 수를 선택한다.(isItlarger)
#두 수를 비교해보고, 더 높은 수를 저장한다.(output)

import time

total_time = 0
output = -9999999999

for i in range(n):
    print("m 길이만큼의 데이터 입력")
    data = list(map(int, input().split()))
    start_time = time.time() #시작 시간
    
    data = sorted(data)
    isItlarger = data[0] #가장 작은 수를 넣어둔다.

    if(isItlarger >= output): #각각의 행에서 나온 '가장 작은 수'를 비교하여서, 더 큰 값을 결과값으로 저장해준다.
        output = isItlarger

    end_time = time.time() #종료 시간
    total_time += (end_time - start_time) #총 시간


print("결과값 : ",output)
print("걸린 시간 : ",total_time)
