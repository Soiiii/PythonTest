# JadenCase 문자열 만들기
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# 공백에 대한 처리를 안해서 틀림
# def solution(s):
#     answer = ''
#     a = list(s.split(' '))
#     print(a)
#     i=0
#     for char in a:
#         if char.isalpha():
#             answer += char.capitalize() + ' '
#         elif char == '':
#             answer
#         else:
#             answer += char + ' '
#     return print(answer[:len(answer)-1])
#
# solution("hello      world")

def solution(s):
    answer = ''
    is_first = True

    for char in s:
        if char.isalpha():
            if is_first:
                answer += char.upper()
                is_first = False
            else:
                answer += char.lower()
        elif char == ' ':
            is_first = True
            answer += char
        else:
            is_first = False
            answer += char.lower()
    return print(answer)
solution("for the last week")