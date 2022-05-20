#풀이
#1. 입력받은 리스트에서, 문자 리스트와 숫자 덧셈 결과로 나누어 저장한다.
#2. 문자 리스트는 오름차순 정렬, 숫자 덧셈 결과는 각각의 값을 더해준다.
#3. 문자 리스트와 숫자 덧셈 결과를 합친다.

#입력 구간
S = input()

#구현 구간
import time
start_time = time.time()

numberDictionary = ['0','1','2','3','4','5','6','7','8','9']
numberAddResult = 0
alphabetList = []

S = list(map(str, str(S)))
for i in range(len(S)):
    if S[i] in numberDictionary:
        numberAddResult += int(S[i])
    else:
        alphabetList.append(S[i])

alphabetList.sort()
alphabetList = ''.join(alphabetList) #리스트를 문자열로 바꾸어준다.
S = []
S = alphabetList + str(numberAddResult)

end_time = time.time()

print(S)
print("경과 시간 : ",end_time - start_time)
