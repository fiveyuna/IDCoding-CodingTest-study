# 백준 / 실버5
# 2693 : N번째 큰 수
# 7분
# https://www.acmicpc.net/problem/2693

T = int(input())
data = [list(map(int, input().split())) for _ in range(T)]

for i in range(T) :
    data[i] = sorted(data[i], reverse=True)
    print(data[i][2])
    