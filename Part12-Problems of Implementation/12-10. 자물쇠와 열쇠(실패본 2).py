def rotate90(key):
    keyRotated = [[0 for col in range(len(key))] for row in range(len(key))]
    N = len(key)-1
    for i in range(len(key)):
        for j in range(len(key)):
            keyRotated[j][N-i] = key[i][j]
    
    return keyRotated

def extendKey(key, lock):
    extendedLength = 2*len(key) + len(lock) - 2
    extendedKey = [[0 for col in range(extendedLength)] for row in range(extendedLength)]
    for i in range(len(key)):
        for j in range(len(key)):
            extendedKey[i][j] = key[i][j]

    return extendedKey

def extendLock(key, lock):
    extendedLength = 2*len(key) + len(lock) - 2
    extendedLock = [[1 for col in range(extendedLength)] for row in range(extendedLength)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            extendedLock[i+len(key)-1][j+len(key)-1] = lock[i][j]
    print(extendedLock)
    return extendedLock

def search(key, lockExtended, rowMoving, colMoving):
    answer = False
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                lockExtended[i+rowMoving][j+colMoving] = key[i][j]
    
    answer = unlocking(lockExtended)
    return answer

def unlocking(lockExtended):
    answer = True
    for i in range(len(lockExtended)):
        for j in range(len(lockExtended)):
            if lockExtended[i][j] == 0:
                answer = False
            if answer == False:
                break
        if answer == False:
            break

    return answer

def solution(key, lock):
    answer = False
    
    lockExtended = extendLock(key, lock)
    
    for i in range(4):
        keyRotated = rotate90(key)
        keyExtended = extendKey(key, lock)

        searchLength = len(key)+len(lock)-2
        for j in range(searchLength):
            for k in range(searchLength):
                answer = search(key,lockExtended, j, k)
                if answer == True:
                    break
            if answer == True:
                break
        if answer == True:
            break

    return answer
        

key = [[1,1],
       [0,0]]
lock = [[1,1,1],
        [0,0,1],
        [1,1,1]]
print(solution(key, lock))

key = [[0,0,0],
       [1,0,0],
       [0,1,1]]
lock = [[1,1,1],
        [1,1,0],
        [1,0,1]]
print(solution(key, lock))
