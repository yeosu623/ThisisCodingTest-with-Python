#11-2. 곱하기 혹은 더하기
#풀이
#0,1은 더하기, 2~9는 곱하기를 한다.

#알고리즘 과정
#1. 숫자를 입력받고, 가장 왼쪽 자릿수를 저장한다.
#2. 그 후 다음 자릿수를 확인한다.
#2. 만약 0,1이면 다음 숫자와 더하기를, 2~9면 곱하기를 한다.
#3. 이 결과를 저장하고, 다음 숫자에 대해 과정을 반복한다.

#단, 결과 값이 0이면, 곱하기가 의미가 없으므로 "무조건 더하기"를 해주어야 한다.

#코드
#시작 구간
S = input()

#풀이 구간
import time
start_time = time.time()

result = int(S[0])

for idx in range(1,len(S)):
    next_number = int(S[idx])

    if result == 0:
        result += next_number
        continue

    if next_number == 0 or next_number == 1:
        result += next_number
    else:
        result *= next_number

#종료 구간
end_time = time.time()

print("결과 값 : ", result)
print("경과 시간 :", end_time - start_time)
