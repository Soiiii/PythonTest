# 연속 부분 수열 합의 개수
# 철호는 수열을 가지고 놀기 좋아합니다.
# 어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수
# 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 원형 수열이란 일반적인 수열에서
# 처음과 끝이 연결된 형태의 수열을 말합니다. 예를 들어 수열 [7, 9, 1, 1, 4] 로
# 원형 수열을 만들면 다음과 같습니다.

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