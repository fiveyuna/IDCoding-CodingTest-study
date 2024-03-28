''' 1419 : love 2
영어 문장이 입력된다.
그 문장에서 love가 몇 번 나오는지 출력하시오.

입력 > 영어 한 문장이 입력된다.(공백 있음, 최대 글자수 100)
출력 > 소문자 love가 몇 번 나오는지 출력한다.

입력예시) love lovely
출력예시) ２
'''

_word = "love"
_word_len = len(_word)
_str = input()
_str_len = len(_str)
_start_index = 0 # 문자열 찾기 시작할 인덱스
_cnt = 0

while _start_index < _str_len:
    _index = _str.find(_word, _start_index)

    if _index < 0:
        break

    _start_index = _index + _word_len
    _cnt += 1

print(_cnt)