#풀이
#리스트를 반으로 나누고, 그 값을 전부 더한다.

#입력 구간
while True:
    score = int(input())
    score = list(map(int, str(score)))
    if len(score) % 2 == 0:
        break

#구현 구간
import time
start_time = time.time()

section_first = score[:len(score)//2]
section_second = score[len(score)//2:]

score_first = 0
score_second = 0

for i in section_first:
    score_first += i
for i in section_second:
    score_second += i

if(score_first == score_second):
    print("LUCKY")
else:
    print("READY")

end_time = time.time()
print("실행 시간 : ",end_time - start_time)
