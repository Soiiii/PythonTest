# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
def factorial(i):
    result = 1
    if i>0:
        result = i * factorial(i-1)
    return result

i = int(input())
print(factorial(i))