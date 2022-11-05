class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return None
        if n == 0:
            return head
        p = head
        q = head
        for i in range(n):
            if q is None:
                return head
            q = q.next
        if q is None:
            return head.next
        while q.next is not None:
            p = p.next
            q = q.next
        p.next = p.next.next
        return head

if __name__ == "__main__":
    head = ListNode(1)
    s = Solution()
    head = s.removeNthFromEnd(head, 1)
    p = head
    while p is not None:
        print(p.val)
        p = p.next