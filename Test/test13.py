# 정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서
# 그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을
# 추가하여 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    print('num_list:',num_list[-1])
    answer = []
    answer = num_list
    if(answer[-2] < answer[-1]):
        num = answer[-1] - answer[-2]
        answer.append(num)
    else:
        num = answer[-1] * 2
        answer.append(num)
    return print(answer)

solution([5, 2, 1, 7, 5])

def solution(l):
    l.append(l[-1] - l[-2] if l[-1] > l[-2] else l[-1]*2)
    return l