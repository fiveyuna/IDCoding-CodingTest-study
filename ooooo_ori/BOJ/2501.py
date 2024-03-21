#백준 2501

N, K = map(int, input().split())

# N의 약수 개수
th = 0 
# N의 K번째 약수
num = 0

for n in range(1,N+1) :
    if(N % n != 0) : 
        continue 
    
    th += 1
    if(K == th) :
        num = n
        break
        
print(num)
            
# num 초기값 0 으로 설정 > 필요없는 코드
# if(K > th) : print(0)
# else : print(num)