''' 1273 : 약수 구하기
자연수 N이 주어지면 N의 약수를 오름차순으로 모두 출력하시오.

입력 > 자연수 N이 입력된다.( 1 <= N <= 10,000 )
출력 > N의 약수를 오름차순으로 출력한다.

입력예시) 6
출력예시) 1 2 3 6
'''

_data = int(input())
_list = []

#for n in range(1, math.sqrt(_data) + 1):
for n in range(1, _data + 1):
    if _data % n == 0:
        _list.append(n)

print(*_list)