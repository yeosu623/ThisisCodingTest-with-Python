#1. rotating
#2. slicing
#3. moving and inserting
#4. unlocking

#다음과 같은 과정까진 맞으나, 시간 초과가 뜬다.
#따라서 다음의 과정을 거친다.

#1. 열쇠의 1 + 자물쇠의 1 = (자물쇠의 길이)^2 // 조건을 추가하여, 차후의 연산을 줄인다. (시간초과 11개 남음)
#2. 그러면 "1의 갯수"도 맞는데, 그 위치와 모양만 확인하면 되므로 "unlocking"은 제외시킬 수 있다. (시간초과 3개 남음)
#3. 열쇠의 길이^2 > 자물쇠의 0의 개수 //조건을 추가하여, 차후의 연산을 줄인다. (시간초과 1개 남음)


def rotating(key, rotating):
    #0=무회전, 1=반시계 90도, 2=반시계 180도, 3=반시계 270도

    #원리
    #3,5 -> N-5, 3 -> N-3, N-5 -> 5, N-3
    #일반화 : a,b -> b, N-a -> N-a, N-b -> N-b, a
    keyRotated = [[0 for col in range(len(key))] for row in range(len(key))]
    N = len(key)-1
    
    if rotating == 0:
        keyRotated = key
    if rotating == 1:
        for i in range(len(key)):
            for j in range(len(key)):
                keyRotated[j][N-i] = key[i][j]
    if rotating == 2:
        for i in range(len(key)):
            for j in range(len(key)):
                keyRotated[N-i][N-j] = key[i][j]
    if rotating == 3:
        for i in range(len(key)):
            for j in range(len(key)):
                keyRotated[N-j][i] = key[i][j]

    return keyRotated

def slicing(key, rowLength, colLength, rowCoordStart, colCoordStart):
    keyRowed = key[rowCoordStart : rowCoordStart + colLength]
    keyColed = []
    for row in keyRowed:
        keyColed.append(row[colCoordStart : colCoordStart + rowLength])
        
    return keyColed

def checkEnoughLength(lock, keyWidth, keyHeight):
    #정답 조건 : 열쇠의 면적 > 자물쇠에서 0의 개수
    lockCount = 0
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == 0:
                lockCount += 1
    if keyWidth * keyHeight >= lockCount:
        return True
    else:
        return False
            

def checkKeyAndLock(key, lock):
    #정답 조건 : 열쇠의 1 + 자물쇠의 1 = (자물쇠의 길이)^2
    keyCount = 0
    for i in range(len(key)):
        for j in range(len(key[0])):
            keyCount += key[i][j]
    lockCount = 0
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            lockCount += lock[i][j]

    if (keyCount + lockCount) == len(lock)*len(lock) :
        return True
    else:
        return False

def movingAndInserting(keySliced, lock, rowCoordOnLock, colCoordOnLock):
    answer = True
    
    for i in range(len(keySliced)):
        for j in range(len(keySliced[0])):
            lockValue = lock[i+rowCoordOnLock][j+colCoordOnLock]
            keyValue = keySliced[i][j]
            if (lockValue == 0 and keyValue == 1) or (lockValue == 1 and keyValue == 0): #열쇠와 자물쇠가 잘 결합되었다.
                continue
            else: #잘 결합이 안됬다.
                answer = False

            if answer == False:
                break
        if answer == False:
            break

    return answer

'''
def unlocking(keyWithLock):
    answer = True
    for i in range(len(keyWithLock)):
        for j in range(len(keyWithLock[0])):
            if not keyWithLock[i][j] == 1:
                answer = False
            if answer == False:
                break
        if answer == False:
            break

    return answer
'''

def solution(key, lock):
    answer=False

    for i in range(4):
        keyRotated = rotating(key, i)

        for rowLength in range(1, len(key)+1):
            for colLength in range(1, len(key)+1):
                
                #정답의 조건을 확인하여, 뒤의 연산을 줄인다.
                doProcess1 = checkEnoughLength(lock, rowLength, colLength)
                if doProcess1 == False:
                    continue
                
                for rowCoordStart in range(len(key)-colLength+1):
                    for colCoordStart in range(len(key)-rowLength+1):
                        keySliced = slicing(keyRotated, rowLength, colLength, rowCoordStart, colCoordStart)

                        #정답의 조건을 확인하여, 뒤의 연산을 줄인다.
                        doProcess2 = checkKeyAndLock(keySliced, lock)
                        if doProcess2 == False:
                            continue
                        
                        for rowCoordOnLock in range(len(lock)-len(keySliced)+1):
                            for colCoordOnLock in range(len(lock[0])-len(keySliced[0])+1):
                                answer = movingAndInserting(keySliced, lock, rowCoordOnLock, colCoordOnLock)

                                '''
                                answer = unlocking(keyWithLock)
                                '''
                                

                                if answer == True:
                                    break
                            if answer == True:
                                break
                        if answer == True:
                            break
                    if answer == True:
                        break
                if answer == True:
                    break
            if answer == True:
                break
        if answer == True:
            break

    return answer

key = [[1,0],
       [1,0]]
lock =[[1,1,1],
       [0,0,1],
       [1,1,1]]
print(solution(key, lock))


key =[[1,1,1],
     [0,0,1],
     [1,1,1]]
lock =[[1,1,1,1],
       [0,0,0,1],
       [0,1,0,1],
       [0,1,0,1]]
print(solution(key,lock))

