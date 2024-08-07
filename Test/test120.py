# 완주하지 못한 선수
#
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는
# 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열
# completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
def solution(participant, completion):
    answer = ''
    hash_dic = {}
    sum = 0
    for i in participant:
        hash_dic[hash(i)] = i
        sum += hash(i)
    for j in completion:
        sum -= hash(j)
    return hash_dic[sum]
    # participant.sort()
    # completion.sort()
    # for i,j in zip(participant, completion):
    #     print(i,j)
    #     if i != j:
    #         return i

solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
# from collections import Counter
# def solution(participant, completion):
#     participant_counter = Counter(participant)
#     completion_counter = Counter(completion)
#
#     difference = participant_counter - completion_counter
#     print(difference.keys())
#     return list(difference.keys()[0])

    # answer = ''
    # for j in participant:
    #     if j not in completion:
    #         return j
    #     elif participant.count(j) > completion.count(j):
    #         return j
