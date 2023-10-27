# 원소들의 곱과 합
# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을
# return 하도록 solution 함수를 완성해주세요.

num_list = [3, 4, 5, 2, 1]
num_list2 = [5, 7, 8, 3]

def aa(num_list):
    a = 0
    b = 1
    for i in num_list:
        print(i)
        a = a+i
        b = b*i
        if(a**2 > b):
            print('1')
        else:
            print('0')

    print('a', a**2)
    print('b', b)

def solution(num_list):
    s=sum(num_list)**2
    m=eval
