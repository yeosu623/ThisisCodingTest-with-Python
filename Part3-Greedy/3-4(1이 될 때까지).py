#3-4(1이 될 때까지)

#입력 조건
print("n, k 입력(2 <= n,k <= 100,000)")
n, k = map(int, input().split())

#알고리즘 선택
#이 문제는 우선적으로 어떤 방법을 택하므로, 탐욕 알고리즘을 사용한다.

#문제 해결 전략
#1번보다 2번을 택하는 것이 "1"을 최대한 빠르게 만들 수 있는 지름길이다.
#따라서 2번을 조건이 만족될 때 마다 바로바로 사용해주어야 한다.
#조건 : n % k == 0

import time
start_time = time.time()

output = 0 #과정의 최소 횟수.

while n != 1:
    if n % k == 0:
        n = n // k
        output += 1
        print(n)
    else:
        n = n - 1
        output += 1
        print(n)

end_time = time.time()

print("결과값 : ", output)
print("경과 시간 : ", end_time - start_time)
