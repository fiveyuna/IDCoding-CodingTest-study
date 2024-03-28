''' 1902 : (재귀 함수) 1부터 n까지 역순으로 출력하기
정수 n부터 1까지 출력하는 재귀함수를 설계하시오.

이 문제는 반복문 for, while 등을 이용하여 풀수 없습니다.
금지 키워드 : for while goto

입력 > 정수 n이 입력된다(1<=n<=200)
출력 > n부터 1까지 한 줄에 하나씩 출력한다.

입력예시) 10
출력예시) 
10
9
8
7
6
5
4
3
2
1
'''

_n = int(input())

# 1부터 n까지 출력하는 함수
def printTo1(now):
    print(now)

    if now == 1: return
    
    now -= 1
    printTo1(now)


printTo1(_n)