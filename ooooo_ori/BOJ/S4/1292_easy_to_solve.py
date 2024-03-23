# 백준 / 실버4
# 1292 : 쉽게 푸는 문제
# 12분
# https://www.acmicpc.net/problem/1292

start, end = map(int, input().split())
data = []
length = 0
sum = 0
i = 0

while length <= end :
    i += 1
    for _ in range(i) :
        data.append(i)        
        length += 1
        
        if start <= length <= end :
            sum += i            

print(sum)

# 이렇게 풀었을 때는 오답이라는데 왜일까요 
# start, end = map(int, input().split())
# data = []
# sum = 0

# for i in range(end) :
#    for _ in range(i) :
#        data.append(i)        
       
#        if start <= len(data) <= end :
#            sum += i            
#        if len(data) == end :
#            break

# print(sum)