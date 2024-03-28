''' 1904 : (재귀함수) 두 수 사이의 홀수 출력하기
시작수(a)와 마지막 수(b)가 입력되면
a부터 b까지의 모든 홀수를 출력하시오.

이 문제는 반복문 for, while 등을 이용하여 풀수 없습니다.
금지 키워드 : for while goto

입력 > 두 수 a , b 가 입력된다. ( 1 <= a <= b <= 100 )
출력 > a ~ b 의 홀수를 모두 출력한다.

입력예시) 2 7
출력예시) 3 5 7
'''
_a, _b = map(int, input().split())

# 두 수 사이의 홀수 출력하는 함수
def printOddToEnd(num, end):
    if num % 2 != 0 :
        print(num)

    if num == end: return
    
    num += 1
    printOddToEnd(num, end)


printOddToEnd(_a, _b)