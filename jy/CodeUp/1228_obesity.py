''' 비만도 측정
* 비만도 계산 공식(브로카의 공식)
표준몸무게 = (실제 키 - 100) * 0.9
비만도 = (실제 몸무게 - 표준몸무게)  * 100 / 표준 몸무게

* 비만도에 따른 등급 판정
등급	        비만도 수치
10이하	        정상
10초과 20이하	과체중
20 초과	        비만

입력예시) 170.0 80.0
출력예시) 비만
'''

inp = input().split()
h, w = float(inp[0]), float(inp[1])

# 비만도 계산
standard_w = (h - 100) * 0.9
obesity = (w - standard_w) * 100 / standard_w

msg = ''
if obesity <= 10:
    msg = '정상'
elif obesity <= 20:
    msg = '과체중'
else:
    msg = '비만'


print(msg)