#1. rotating
#2. slicing
#3. moving and inserting
#4. unlocking

import copy

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

def movingAndInserting(keySliced, lock, rowCoordOnLock, colCoordOnLock):
    for i in range(len(keySliced)):
        for j in range(len(keySliced[0])):
            lock[i+rowCoordOnLock][j+colCoordOnLock] += keySliced[i][j]

    return lock

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

def solution(key, lock):

    for i in range(4):
        keyRotated = copy.deepcopy(rotating(key, i))

        for rowLength in range(1, len(key)+1):
            for colLength in range(1, len(key)+1):
                for rowCoordStart in range(len(key)-1):
                    for colCoordStart in range(len(key)-1):
                        keySliced = slicing(keyRotated, rowLength, colLength, rowCoordStart, colCoordStart)
                        
                        for rowCoordOnLock in range(len(lock)-len(keySliced)+1):
                            for colCoordOnLock in range(len(lock[0])-len(keySliced[0])+1):
                                keyWithLock = movingAndInserting(keySliced, copy.deepcopy(lock), rowCoordOnLock, colCoordOnLock)

                                answer = unlocking(keyWithLock)

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

key = [[1,1],
       [0,0]]
lock =[[1,1,1],
       [0,0,1],
       [1,1,1]]
print(solution(key, lock))


key =[[1,1,1],
     [0,0,1],
     [1,1,1]]
lock =[[1,1,1,1],
       [0,0,0,1],
       [1,1,0,1],
       [0,0,0,1]]
print(solution(key,lock))

