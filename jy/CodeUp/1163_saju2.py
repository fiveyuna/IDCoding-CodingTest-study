import math

# (년 + 월 + 일)에 100의 자리 숫자가 짝수이면 "대박", 그렇지 않으면 "그럭저럭"을 출력
# 입력예시) 1502 2 10
# 출력예시) 그럭저럭

str = input()
list = str.split()

num = int(list[0]) + int(list[1]) + int(list[2])

# 백의 자리 이상 숫자만 남김(예: 1514 -> 15)
num = math.trunc(num/100)

if num%2 == 0: # 짝수면
    print("대박")
else :
    print("그럭저럭")
