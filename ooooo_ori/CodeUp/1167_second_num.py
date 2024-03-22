# 코드업 
# 1167 : 두 번째 수
# 15분

# data = input().split() > 결과 다름
# 5 9 2 > 2 5 9 > 5 출력 
# 201 20 3 > 20 201 3 > 201 출력
# 이유 : ! int 형 list로 만들어주지 않아서 같은데,, 멋진 설명이 안 떠오르네요!

# data = input().split() #int 로 바꾸면 풀릴 듯 #map 만 했을 때
# data = map(int, input().split())

# 1 : map 사용 시 sort 불가능 > sorted 사용
# data = map(int, input().split())
# data = sorted(data)

# 2 : list 사용 시 sort 가능 > sort 사용 (sr)
data = list(map(int, input().split()))
# data.sort() #list 여야 가능 map 은 sort 안 됨
data = sorted(data)

print(data[1])
