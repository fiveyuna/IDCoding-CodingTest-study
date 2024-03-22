# 백준 / 브론즈3
# 10818 : 최소, 최대
# 5분

n = int(input())
nums_list = list(map(int, input().split()))

sorted = sorted(nums_list)
print(sorted[0], sorted[n-1])
