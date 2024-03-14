''' 비만도 측정2
* 비만도 계산 공식
비만도 = (실제 몸무게 - 표준몸무게)  * 100 / 표준 몸무게

* 표준몸무게
키에 따른 표준몸무게	    공식
키가 150 미만일 때          (실제 키 - 100)
키가 150이상 160미만일 때   (실제 키 - 150) /2 + 50
키가 160 이상일 때          (실제 키 - 100) * 0.9

* 비만도에 따른 등급 판정
비만도	        등급
10 이하	        정상
10 초과 20 이하 과체중
20 초과	        비만

입력예시) 150 60
출력예시) 과체중
'''

inp = input().split()
h, w = float(inp[0]), float(inp[1])

# 비만도 계산
standard_w = 0
if h < 150:
    standard_w = h - 100
elif h <160:
    standard_w = (h - 150)/2 + 50
else:
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