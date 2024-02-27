# N개의 최소공배수
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
# 예를 들어 2와 7의 최소공배수는 14가 됩니다.
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수,
# solution을 완성해 주세요.
# 제한 사항
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.

def solution(arr):
    max_num = max(arr)  # 주어진 배열에서 가장 큰 숫자를 찾습니다.
    lcm = max_num  # 초기 최소 공배수는 가장 큰 숫자로 설정합니다.
    print('origin', lcm)
    print('origin', max_num)
    while True:
        if all(lcm % num == 0 for num in arr):  # 모든 숫자의 배수인지 확인합니다.
            return lcm  # 최소 공배수를 찾으면 반환합니다.
        print('lcm',lcm)
        lcm += max_num  # 아니라면 최소 공배수를 증가시킵니다.
