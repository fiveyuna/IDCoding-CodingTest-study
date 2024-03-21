# 코드업 
# 1167 : 두 번째 수
# 20분

# data = input().split() > 결과 다름
# 5 9 2 > 2 5 9 > 5 출력 
# 201 20 3 > 20 201 3 > 201 출력
# 이유 : ! int 형 list로 만들어주지 않아서 같은데,, 멋진 설명이 안 떠오르네요!

#data = input().split()
data = list(map(int, input().split()))
data.sort()

print(data[1])
