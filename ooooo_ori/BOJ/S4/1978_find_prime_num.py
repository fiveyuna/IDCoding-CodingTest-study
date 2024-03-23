# 백준 / 실버4
# 1978 : 소수 찾기
# 10분 
# https://www.acmicpc.net/problem/1978

N = int(input())
data = list(map(int, input().split()))
cnt = N

for i in range(N) :
    if data[i] == 1 :
        cnt -= 1
        continue
    
    for j in range(2, data[i]):
        if data[i] % j == 0 :
            cnt -= 1
            break
        
print(cnt)
