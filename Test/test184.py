# 문자열안에 문자열
# 문자열 str1, str2가 매개변수로 주어집니다.
# str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

def solution(str1, str2):
    answer = 0
    if str2 in str1:
        return 1
    else:
        return 2
    return answer