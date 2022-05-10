#큰 수의 법칙
#(시작시간 : 2시 10분)

#입력 조건
print("n m k 입력")
n, m, k = map(int, input().split())
print("배열의 데이터 입력")
data = list(map(int, input().split()))

import time
start_time = time.time()

#알고리즘 과정
#규칙적으로 수를 더하므로 "탐욕 알고리즘(Greedy Algorithm)"을 사용할 수 있다.

#문제풀이 과정
#조건 1. 가장 큰 수가 단일로 존재하고, 두번째로 큰 수가 존재할 때
#가장 큰 수를 K번 더한 후, 두번째로 큰 수를 더하는 식으로 반복한다.

#조건 1 식 세우기
#가장 큰 수 = first, 두번째로 큰 수 = second 라고 하자.
#K는 "배수"로 인식하면 문제를 더 쉽게 풀 수 있다.
#그러면 first를 M번 반복하는데, first-second의 값을 K만큼 반복하여 빼준다.
#그러면 식은 first*M - (first-second)*(M//K)

data = sorted(data, reverse=True)
first = data[0]
second = data[1]

if(first != second):
    output = first * m - (first-second) * (m//k)

#조건 2. 가장 큰 수와 두번째로 큰 수가 동일할 때
#그 수를 M번 곱하면 된다.

#조건 2 식 세우기
#first*M
if(first == second):
    output= first * m

end_time = time.time()
print("결과 : ", output)
print("프로그램 실행 시간 : ", end_time - start_time)


