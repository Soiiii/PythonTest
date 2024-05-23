# 체육복
#
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in reserve:
        print('i', i)
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    for i in reserve:
        if i -1 in lost:
            lost.remove(i-1)
        elif i + 1 in lost:
            lost.remove(i+1)

    answer = n - len(lost)
    return answer