
# 중앙값 구하기
# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때,
# array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
def solution(array):
    answer = 0
    array.sort()
    print(array)
    answer = array[int(len(array) / 2)]
    return answer