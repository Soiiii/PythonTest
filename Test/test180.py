# 이어 붙인 수
# 정수가 담긴 리스트 num_list가 주어집니다.
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return
# 하도록 solution 함수를 완성해주세요.

num_list=[3, 4, 5, 2, 1]
a = ''
b = ''
for i in num_list:
    if(i % 2 == 1):
        a = a + '' + str(i)
        print('홀수',a)
    else:
        b = b + '' + str(i)
        print('짝수',b)
print(int(a) + int(b))