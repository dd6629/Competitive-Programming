# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        k %= length
        if k == 0:
            return head
        current.next = head
        snt = length - k - 1
        new_tail = head
        for i in range(snt):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
        
        