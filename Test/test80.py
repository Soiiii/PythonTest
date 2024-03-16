# 괄호 회전하기
# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
# (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다.
# 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다.
# 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다.
# 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호
# 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

def solution(elements):
    answer = 0
    # 원형 수열을 두 배로 늘림
    elements *= 2
    total = set()

    # 연속 부분 수열을 구하고 합을 total에 추가
    for start in range(len(elements)):
        for length in range(1, len(elements) // 2 + 1):
            subsequence = elements[start:start + length]
            total.add(sum(subsequence))

    # 중복을 제거한 후, 총 개수 반환
    return len(total)

    # 1~len(i) 번째의 합
    # elements.sort()
    # total = set()
    # sortedElements = sorted(elements)
    # print('sortedElements', sortedElements)
    # while True:
    #     for i in range(1, len(sortedElements)+1):
    #         for j in range(len(sortedElements)):
    #             total.add(sortedElements[j])
    # print(total)

    # for i in sortedElements:
    #     total[i] = total.get(i, 0) + 1
    # print('total', total)
    # for j in total:
    #     print('j',j,'total.get(j)', total.get(j))
    #     for jj in range(1, len(total)+1):
    #         answer += total.get(j)
    print('answer', answer)
    return answer