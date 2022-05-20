#풀이
#1. 자물쇠의 홈 > 열쇠의 걸쇠 : 홈이 남으므로 답이 없다.
#2. 자물쇠의 홈 == 열쇠의 걸쇠 : 열쇠를 회전해보고, 일치시켜본다.
#네 가지 경우의 수가 있다. 일반, 시계 90도, 시계 180도, 시계 270도.
#3. 자물쇠의 홈 < 열쇠의 걸쇠
#M-1, M-1 크기의 열쇠를 시험해보고, 1,2,3 번을 반복한다.
#네 가지 경우의 수가 있다. 11~M-1M-1, 12~M-1M, 21~MM-1. 22~MM
import numpy as np
import time

def counting(arr, zeroOrOne):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == zeroOrOne:
                count += 1
    print("count:",count)

    return count

def unlocking(originKey, lock):

    for i in range(4):
        key = originKey
        print("OriginKey:", key)
        key = rotating(key, i)
        print("rotatedkey:", key)
        for j in range(len(lock)-len(key)):
            for k in range(len(lock)-len(key)):
                key = movingAndFlatting(key, lock, j, k)
                print("movingAndFlattingkey:",key)
                print("FinalKey:",key)
                print("FinalLock:",lock)

                result = key + lock
                print("result:",result)
                if np.all(result==1):
                    return True
                
    return False

def rotating(key, rotating):
    #0=무회전, 1=반시계 90도, 2=반시계 180도, 3=반시계 270도

    #원리
    #3,5 -> N-5, 3 -> N-3, N-5 -> 5, N-3
    #일반화 : a,b -> N-b, a -> N-a, N-b -> b, N-a
    keyRotated = [[0 for col in range(len(key))] for row in range(len(key))]
    N = len(key)-1
    
    if rotating == 0:
        keyRotated = key
    if rotating == 1:
        for i in range(len(key)):
            for j in range(len(key)):
                keyRotated[N-j][i] = key[i][j]
    if rotating == 2:
        for i in range(len(key)):
            for j in range(len(key)):
                keyRotated[N-i][N-j] = key[i][j]
    if rotating == 3:
        for i in range(len(key)):
            for j in range(len(key)):
                keyRotated[j][N-i] = key[i][j]

    return keyRotated

        
def movingAndFlatting(key, lock, xMoving, yMoving):
    print("1")
    keyTemplate = [[0 for col in range(len(lock))] for row in range(len(lock))]
    print(keyTemplate)
    for i in range(len(lock)):
        for j in range(len(lock)):
            print("i+xMoving", i+xMoving)
            print("j+yMoving", j+yMoving)
            keyTemplate[i][j] = key[i+xMoving][j+yMoving]
            print(keyTemplate)

    return keyTemplate

def solution(key, lock):
    answer = False

    key = np.array(key)
    lock = np.array(lock)

    lock0Count = counting(lock, 0)
    key1Count = counting(key, 1)

    if lock0Count > key1Count :
        pass
    if lock0Count == key1Count:
        answer = unlocking(key, lock)
        if answer == True:
            return answer

key = [[1,1],[0,0]]
lock = [[1,0,1],[1,0,1],[1,1,1]]
start_time = time.time()
print(solution(key, lock))
end_time = time.time()
print("경과 시간 : ", end_time - start_time)
