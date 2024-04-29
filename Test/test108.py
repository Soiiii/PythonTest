# 이상한 문자 만들기
#
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후,
# 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.


# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로,
# 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

def solution(s):
    bb = s.split(' ')
    for h,j in enumerate(bb):
        aa = list(j)
        for k,i in enumerate(j):
            aa.pop(k)
            if k % 2 == 0:
                aa.insert(k,i.upper())
            else:
                aa.insert(k,i.lower())
        bb.pop(h)
        strA = ''.join(aa)
        bb.insert(h,strA)
    return ' '.join(bb)