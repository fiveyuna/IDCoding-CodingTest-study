# 코드업 
# 1172 : 세 수 정렬하기
# 15분

num = map(int, input().split())
num = sorted(num)

# 다른 풀이 참고
print(*num)

# 기존 내 풀이 > 출력 : [6, 7, 8]
# print(num)

# 다른 사람 풀이 1 > 출력 : 6 7 8
# print(str(num[0]) + ' ' + str(num[1]) + ' ' + str(num[2]))

# 다른 사람 풀이 2 > 출력 : 6 7 8
# for i in num : 
#   print(i, end = ' ')
