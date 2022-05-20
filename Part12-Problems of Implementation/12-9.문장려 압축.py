#풀이
#모든 경우의 수(1)로 문자열을 나누어 보면서, 각각의 경우를 저장한다.
#그 중 제일 짧은 답을 택하면 된다.
#알고리즘
#1. 1부터 최대 길이 까지 반복문을 작성
#2. 현재 문자열을 잘라두고, 다음 문자열을 "미리 확인"한다.
#3. 만약 두 구간이 같으면, 반복 횟수를 저장
# 반복이 같지 않으면 임시 문자열에 저장

#(1) 주석. 모든 경우의 수가 아닌, "문자열 길이의 절반" 만큼만 확인한다.
#그 이유는, 문자열 길이의 절반보다 더 큰 정수로 쪼갤경우, 문자열을 압축할 수 없기 때문이다.
#이러면 연산 횟수를 절반이나 줄일 수 있다.
#예시 : len(s) = 10, sliceLength = 5
#len(s) = 11, sliceLength = 5
#즉, len(s) // 2

def solution(s):
    answer = 99999999
    #문자열의 길이가 0 혹은 1일 경우, 답은 0 혹은 1
    if(len(s) <= 1):
        answer = len(s)
        return answer
    
    #문자열을 자를 최대 정수 설정
    MaxSliceLength = len(s) // 2

    for nowSliceLength in range(1, MaxSliceLength+1):
        print("현재 문자열 자르는 길이 : ", nowSliceLength)
        #초깃값
        sCopy = s
        sectionRepeat = 1
        zipped_s = ""
        
        while True:
            #현재 문자열 자르기, 다음 문자열 확인하기
            nowSection = sCopy[0:nowSliceLength]
            nextSection = sCopy[nowSliceLength:nowSliceLength*2]
            
            sCopy = sCopy[nowSliceLength:]
            
            print("nowSection : ", nowSection)
            print("NextSection : ", nextSection)
            #두 구간이 같으면, 반복 횟수를 저장
            if(nowSection == nextSection):
                sectionRepeat += 1
            #반복이 같지 않으면 임시 문자열에 저장
            else:
                if sectionRepeat == 1:
                    zipped_s = zipped_s + nowSection
                    print("zipped_s", zipped_s)
                else:
                    zipped_s = zipped_s + str(sectionRepeat) + nowSection
                    sectionRepeat = 1
                    print("zipped_s", zipped_s)

            #마지막 문자열인지 확인
            if nextSection == "":
                break

        #결과 확인
        if answer > len(zipped_s):
            answer = len(zipped_s)

    return answer

s = "a"
print(solution(s))
            
        
