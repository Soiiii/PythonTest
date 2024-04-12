# H-Index
#
# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
# 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
# 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
# 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
# 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 기준으로 내림차순 정렬
    h_index = 0  # 초기 H-Index 값을 0으로 설정

    print(citations)
    for i, citation in enumerate(citations):
        if citation >= i + 1:  # 현재 인용 횟수가 논문의 순서보다 크거나 같으면 H-Index 증가
            print(i, citation)
            h_index += 1
        else:
            break  # 조건을 만족하지 않으면 반복문 종료

    return h_index