# 할인 행사
#
# XYZ 마트는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여합니다.
# XYZ 마트에서는 회원을 대상으로 매일 한 가지 제품을 할인하는 행사를 합니다.
#  할인하는 제품은 하루에 하나씩만 구매할 수 있습니다. 알뜰한 정현이는 자신이 원하는 제품과
#  수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다.
#   예를 들어, 정현이가 원하는 제품이 바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개,
# 냄비 1개이며, XYZ 마트에서 14일간 회원을 대상으로 할인하는 제품이 날짜 순서대로
#  치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나인
#  경우에 대해 알아봅시다. 첫째 날부터 열흘 간에는 냄비가 할인하지 않기 때문에 첫째 날에는
#  회원가입을 하지 않습니다. 둘째 날부터 열흘 간에는 바나나를 원하는 만큼 할인구매할 수 없기
#  때문에 둘째 날에도 회원가입을 하지 않습니다. 셋째 날, 넷째 날, 다섯째 날부터 각각 열흘은
#  원하는 제품과 수량이 일치하기 때문에 셋 중 하루에 회원가입을 하려 합니다.
#   정현이가 원하는 제품을 나타내는 문자열 배열 want와 정현이가 원하는 제품의 수량을 나타내는
#  정수 배열 number, XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount가 주어졌을 때,
#  회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는
#   solution 함수를 완성하시오. 가능한 날이 없으면 0을 return 합니다.

# 정답
def solution(want, number, discount):
    answer = 0
    pp = []
    # 모든 가능한 시작 날짜를 반복
    for i in range(len(discount) - 9):  # 10일 연속성을 고려하여 범위 설정
        match = True  # 모든 제품을 할인 받을 수 있는지 여부

        # 각각의 원하는 제품에 대해 검사
        for k in range(len(want)):
            # 할인 제품 리스트에서 10일 동안의 제품 개수를 세고, 원하는 제품과 일치하는지 확인
            if discount[i:i + 10].count(want[k]) < number[k]:
                match = False
                break  # 일치하지 않으면 바로 종료

        # 모든 제품을 할인 받을 수 있고, 중복되지 않은 회원 가입일이라면 pp 리스트에 추가
        if match and i not in pp:
            pp.append(i)

    answer = len(pp)  # 가능한 회원 가입 일수는 pp 리스트의 길이와 동일
    return answer

# 오답
def solution(want, number, discount):
    answer = 0
    pp = []
    for k in range(len(want)):
        for i in range(len(discount)):
            if discount[i:i+10].count(want[k]) == number[k] and len(discount[i:i+10]) == 10:
                pp.append(i)
            else:
                break
    for i in range(len(pp)):
        if pp.count(i) == len(want):
            answer += 1
    return answer

