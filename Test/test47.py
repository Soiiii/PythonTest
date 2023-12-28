# 첫 번째로 나오는 음수
# 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요.
# 음수가 없다면 -1을 return합니다.

def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1

def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
        elif i == len(num_list)-1:
            if num_list[i] > 0:
                return -1

solution([12, 4, 15, 46, 38, -2, 15])