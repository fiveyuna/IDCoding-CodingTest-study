''' 1510 : 홀수 마방진
마방진(magic square)이란 가로, 세로, 대각선의 합이 같은 사각형을 말한다.
홀수 n을 입력으로 받아 n*n 홀수 마방진을 만들어 보자.

만드는 방법은 여러가지 방법이 있지만, 아래와 같은 방법을 이용하여 구현해보자.
구현 방법:
1. 시작은 첫 행, 한 가운데 열에 1을 둔다.
2. 행을 감소, 열을 증가하면서 순차적으로 수를 넣어간다.
3. 행은 감소하므로 첫 행보다 작아지는 경우에는 마지막 행으로 넘어간다.
4. 열은 증가하므로 마지막 열보다 커지는 경우에는 첫 열로 넘어간다.
5. 넣은 수가 n의 배수이면 행만 증가한다. 열은 변화없음.

입력 > 마방진의 크기인 n이 입력된다.(n은 50보다 작은 홀수인 자연수)
출력 > 위의 방법대로 크기가 n인 홀수 마방진을 출력한다.

입력예시) 3
출력예시) 
8 1 6 
3 5 7 
4 9 2 
'''

_n = int(input())
_square = [[0 for col in range(_n)] for row in range(_n)]
_i = 0 # 행
_j = _n//2 # 열
_num = 1

# 인덱스 계산 함수
def calc(size, i, n):
    i += n
    if i < 0 : i += size
    elif i == size : i = 0
    return i

# 마방진 채우기
while _num <= _n*_n:
    _square[_i][_j] = _num

    if _num%_n == 0:
        _i = calc(_n, _i, 1)
    else:
        _i = calc(_n, _i, -1)
        _j = calc(_n, _j, 1)

    _num += 1

# 출력
for i in range(_n):
    for j in range(_n):
        print(_square[i][j], end=" ")
    print()