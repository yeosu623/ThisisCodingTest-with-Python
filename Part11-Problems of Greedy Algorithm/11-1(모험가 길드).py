#11-1. 모험가 길드
#풀이
#X가 작은 사람일 수록 그룹 형성에 유리하다.

#알고리즘
#1. X를 올림차순으로 정렬한다.
#2. 한 사람씩 그룹에 넣는다. 이 때 그 사람의 X를 체크한다.
#3. 그룹 사람과 X가 같아지면 그룹으로 묶어준다.
#4. 이 과정을 N번만큼 반복한다.

#코드
#시작 구간
N = int(input())
people = list(map(int, input().split()))

#해결 구간
import time
start_time = time.time()

people.sort()

count = 0
group = 0

for idx in range(N):
    X = people[idx] #현재 그룹 형성에 필요한 공포도를 측정
    count += 1

    if(X == count):
        group += 1
        count = 0

#종료 구간
end_time = time.time()

print("그룹 수 : ", group)
print("경과 시간 : ", end_time - start_time)
