import time

n = 1260 #거스름돈
count = 0 #동전의 개수
coin_types = [500,100,50,10] #동전의 종류

start_time = time.time()

for coin in coin_types:
    count += n // coin #몫. 동전의 개수 세기
    n %= coin #나머지. x원의 동전을 바꾼 후의 나머지.

print(count)

end_time = time.time()
print("프로그램 작동 시간 : ", end_time - start_time)
    
