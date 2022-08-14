# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseLL(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        mid = self.getMid(head)
        temp = mid.next
        mid.next = self.reverseLL(temp)
        head1 = head
        head2 = mid.next
        while head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        temp = mid.next
        mid.next = self.reverseLL(temp)
        return True


if __name__ == "__main__":
    arr = [1, 2]
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    print(Solution().isPalindrome(head))
