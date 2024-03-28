''' 1286 : 최댓값, 최솟값
5개의 정수들의 최댓값과 최솟값을 구하는 프로그램을 작성하라.

입력예시) 
3
7
-4
-6
5
출력예시) 
7
-6
'''

_data = [int(input()) for _ in range(5)]
_min = 1000000
_max = -1000000

for n in _data:
    if n < _min:
        _min = n
    if n > _max:
        _max = n

print(_max)
print(_min)