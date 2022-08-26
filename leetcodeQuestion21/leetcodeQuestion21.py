# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr1 = list1
        next1 = curr1.next
        curr2 = list2

        while next1 and curr2:
            if curr2.val >= curr1.val and curr2.val <= next1.val:
                curr1.next = curr2
                next2 = curr2.next
                curr1.next.next = next1

                curr1 = curr2
                next1 = curr1.next
                curr2 = next2
            else:
                curr1 = next1
                next1 = curr1.next

        if not next1:
            curr1.next = curr2
            return list1
        return list1

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            return self.solve(list1, list2)
        else:
            return self.solve(list2, list1)

    # driver code
    def __init__(self) -> None:
        n1, n2 = [2], [1]
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
        gg = self.mergeTwoLists(l1, l2)
        for i in range(len(n1) + len(n2)):
            print(gg.val)
            gg = gg.next


Solution()
