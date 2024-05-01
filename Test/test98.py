# 괄호 회전하기
#
# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
# (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다.
# 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다.
# 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다.
# 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가
# 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.
#
def solution(s):
    answer = 0
    s = list(s)
    for _ in range(len(s)):
        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == '[' and s[i] == ']': stack.pop()
                elif stack[-1] == '{' and s[i] == '}': stack.pop()
                elif stack[-1] == '(' and s[i] == ')': stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        if len(stack) == 0:
            answer += 1
        s.append(s.pop(0))
print(solution("[](){}"))

def bracket(s):
    stack = []
    listA = list(s)
    # for i in range(len(listA)):
    stack.append(listA[0])
    listA.pop(0)
    listA.append(stack[0])
    stack.clear()
    dict = {"(":")","{":"}","[":"]"}
    print(dict.get("("))
    # for i in listA:
    #     if i == "(" :
    #         dict.get("(")
    #
    #     elif i == dict("{"):
    #
    #     elif i == dict("["):

# bracket("[](){}")