# 인덱스 바꾸기
#
# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
# my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

def solution(my_string, num1, num2):
    answer = ''
    aa = list(my_string)
    # bb = []
    # bb.append(aa[num1])
    # bb.append(aa[num2])
    aa[num1], aa[num2] = aa[num2], aa[num1]
    # aa[num2] = bb[0]
    answer = "".join(str(element) for element in aa)
    return answer