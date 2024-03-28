''' 1371 : 마름모 출력하기
n이 입력되면 대각선 2개의 길이가 2n인 마름모를 출력하시오.

입력 > 정수 n이 입력된다. ( 2 <= n <= 100 )
출력 > 대각선 2개의 길이가 2n인 마름모를 출력한다.

입력예시) 5
출력예시)
    **
   *  *
  *    *
 *      *
*        *
*        *
 *      *
  *    *
   *  *
    **
'''

_n = int(input())
_2n = _n * 2

for i in range(_2n):
    if i < _n:
        a = _n - i - 1
        b = _2n - a - 1
    else:
        a = i - _n
        b = _2n - a - 1

    for j in range(_2n):
        if j == a or j == b:
            print('*', end="")
        else:
            print(' ', end="")
    print()
