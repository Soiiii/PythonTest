# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
# 작성해야 하는 함수는 다음과 같다.
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

def bb(b:list) -> int:
    #파라미터 타입 명시가 안되어 있어서
    #b:list 라고 선언
    # -> int 정수 타입만 받겠다 뜻
    num = 0
    print(b)
    for x in b:
        num += x
        print(num)

a = list(map(int, input().split()))
#a라는 변수를 사용해서
bb(a)
#bb 함수 실행 값은 a로..

# 1 3 5
# [1, 3, 5]
# 1
# 4
# 9

