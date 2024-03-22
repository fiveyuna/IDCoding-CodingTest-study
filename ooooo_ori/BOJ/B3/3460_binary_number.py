# 백준 / 브론즈3
# 3460 : 이진수
# 1시간 over > 답 참고 

T = int(input())

# 다른 사람 풀이 1
while T > 0 :
    temp = int(input())
    results = []
    cnt = 0
    
    while temp > 0 :
        if(temp % 2 == 1):
            results.append(cnt)
        temp //= 2
        cnt += 1

    print(' '.join(map(str, results)))
    T -= 1

# 다른 사람 풀이 2
for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end = " ")

