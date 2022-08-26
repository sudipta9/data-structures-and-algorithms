from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeUtil(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        current1 = list1
        next1 = current1.next
        current2 = list2
        while next1 and current2:
            if current2.val >= current1.val and current2.val <= next1.val:
                current1.next = current2
                next2 = current2.next
                current2.next = next1
                current1 = current1.next
                current2 = next2
                next1 = current1.next
            else:
                current1 = next1
                next1 = current1.next
        if not next1:
            current1.next = current2
        return list1

    def merge(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            return self.mergeUtil(list1, list2)
        else:
            return self.mergeUtil(list2, list1)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not len(lists):
            return
        last = len(lists) - 1
        while last:
            i, j = 0, last
            while i < j:
                temp1 = lists[i]
                temp2 = lists[j]
                lists[i] = self.merge(temp1, temp2)
                i += 1
                j -= 1
                if i >= j:
                    last = j
        return lists[0]

    # driver code
    def __init__(self) -> None:
        n1, n2, n3 = [1, 5, 7], [2, 3, 6, 9], [4, 8, 10]
        l1 = ListNode(n1[0])
        l2 = ListNode(n2[0])
        l3 = ListNode(n3[0])

        temp = l1
        for i in range(1, len(n1)):
            temp.next = ListNode(n1[i])
            temp = temp.next

        temp = l2
        for i in range(1, len(n2)):
            temp.next = ListNode(n2[i])
            temp = temp.next

        temp = l3
        for i in range(1, len(n3)):
            temp.next = ListNode(n3[i])
            temp = temp.next
        temp = self.mergeKLists([l1, l2, l3])
        while temp:
            print(temp.val)
            temp = temp.next


Solution()
