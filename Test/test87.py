# 없는 숫자 더하기
# 0부터 9까지의 숫자 중 일부가 들어있는 정수
# 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를
# 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = True
    numbers.sort()
    result = 0
    all = [0,1,2,3,4,5,6,7,8,9]
    print(numbers)
    #     0,1,2,3,4,5,6,7,8,9 가 있는 all
    #     0,1,2,3,4,  6,7,8 두가지를 비교
    for i in all:
        for j in numbers:
            print('i',i,'j',j)
            if i == j:
                break
            elif all[-1] == i:
                result += j
    print(result)
    # if j in k:
    #     print('324342')
    return answer