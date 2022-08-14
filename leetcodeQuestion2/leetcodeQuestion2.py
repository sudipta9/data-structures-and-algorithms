# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLL(self, head: Optional[ListNode]):
        current = head
        prev = None
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # l1 = self.reverseLL(l1)
        # l2 = self.reverseLL(l2)
        temp = l1.val + l2.val
        sum = ListNode(temp % 10)
        carry = temp // 10
        l1 = l1.next
        l2 = l2.next
        sumHead = sum
        while l1 and l2:
            temp = (l1.val + l2.val) + carry
            sumHead.next = ListNode(temp % 10)
            carry = temp // 10
            sumHead = sumHead.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            temp = l1.val + carry
            sumHead.next = ListNode(temp % 10)
            carry = temp // 10
            sumHead = sumHead.next
            l1 = l1.next
        while l2:
            temp = l2.val + carry
            sumHead.next = ListNode(temp % 10)
            carry = temp // 10
            sumHead = sumHead.next
            l2 = l2.next
        if carry:
            sumHead.next = ListNode(carry)
            carry = 0
            sumHead = sumHead.next
        return sum


if __name__ == "__main__":
    n1, n2 = [2, 4, 9], [5, 6, 4, 9]
    l1 = ListNode(n1[0])
    l2 = ListNode(n2[0])
    temp = l1
    for i in range(1, len(n1)):
        temp.next = ListNode(n1[i])
        temp = temp.next
    temp = l2
    for i in range(1, len(n2)):
        temp.next = ListNode(n2[i])
        temp = temp.next
    sum = Solution().addTwoNumbers(l1, l2)
    while sum:
        print(sum.val, end=",")
        sum = sum.next
