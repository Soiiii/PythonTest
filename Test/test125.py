# OX퀴즈
#
# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열
# quiz가 매개변수로 주어집니다. 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로
# 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(quiz):
    answer = []
    for q in quiz:
        x, op, y, equal, z = q.split()
        x = int(x)
        y = int(y)
        z = int(z)

        if op == '+':
            if x + y == z:
                answer.append('O')
            else:
                answer.append('X')
        elif op == '-':
            if x - y == z:
                answer.append('O')
            else:
                answer.append('X')

    return answer

def solution(quiz):
    answer = []
    quiz[0].split("-")
    for k,i in enumerate(quiz):
        cc = i.split("=")
        if " +" in cc[0]:
            bb = cc[0].split("+")
            if int(bb[0]) + int(bb[1]) == int(cc[1]):
                answer.append("O")
            else:
                answer.append("X")
        elif "-" in cc[0]:
            bb = cc[0].split("-")
            if int(bb[0]) - int(bb[1]) == int(cc[1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer