# 대문자와 소문자
# 문자열 my_string이 매개변수로 주어질 때,
# 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.


def solution(my_string):
    # 변환된 문자열을 저장할 리스트
    result = []

    # 주어진 문자열의 각 문자를 순회
    for char in my_string:
        # 문자가 대문자이면 소문자로 변환
        if char.isupper():
            result.append(char.lower())
        # 문자가 소문자이면 대문자로 변환
        elif char.islower():
            result.append(char.upper())
        else:
            # 그 외의 경우 (예: 숫자, 공백 등) 변환하지 않고 그대로 추가
            result.append(char)

    # 리스트를 문자열로 변환하여 반환
    return ''.join(result)
