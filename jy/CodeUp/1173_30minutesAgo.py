'''
수호는 30분 전으로 돌아가고 싶은 1人 이다.
공백을 기준으로 시간과 분이 주어진다.
그러면 이 시간을 기준으로 30분전의 시간을 출력하시오.
예) 12 35  =====> 12 5
    12 0 ======> 11 30
    11 5 ======> 10 35
    0 10 ======> 23 40
(시의 범위 : 0~ 23)
(분의 범위 : 0~ 59)
'''

str = input().split()
time, minute = int(str[0]), int(str[1])

if minute >= 30:
    minute -= 30
else:
    minute += 30
    time = 23 if time == 0 else time-1

print(time, minute)