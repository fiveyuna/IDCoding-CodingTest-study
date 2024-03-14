# (년 - 월 + 일)에 마지막 숫자가 0이면 "대박", 그렇지 않으면 "그럭저럭"을 출력
# 입력예시) 1902 2 10
# 출력예시) 대박

str = input()

list = str.split()

num = int(list[0]) - int(list[1]) + int(list[2])

if num%10 == 0: # 10으로 나눈 나머지가 0이면
    print("대박")
else :
    print("그럭저럭")
