# Add Two Numbers
#
# You are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in
# reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode() #ListNode로 초기화 - 더미 노드가 된다
        s = answer #ListNode를 가리키는 포인터
        carry = 0 #올림수 초기화

        #l1나 l2의 자릿수가 남았거나 (이들이 가리키는 값이 null이 아님)
        #처리해줘야 할 올림수가 있거나
        while l1 or l2 or carry:
            sum = 0 # 각 자릿수의 합
            if l1:
                sum += l1.val # 현재 l1 자릿수를 더해주고
                l1 = l1.next # l1의 다음 자릿수를 가리켜준다
            if l2:
                sum += l2.val # 현재 l2 자릿수를 더해주고
                l2 = l2.next # l2의 다음 자릿수를 가리켜준다
            sum += carry # 올림수가 있다면 더해줌
            carry = sum // 10 # 각 자릿수의 합 + 올림수가 두자리가 되면, 올림수 구해줌
            sum = sum % 10
            s.next = ListNode(sum) # 현재 가리키는 노드에 새로운 노드를 연결시켜준다
            s = s.next
        return answer.next # 더미노드 이후의 노드부터 리턴해준다