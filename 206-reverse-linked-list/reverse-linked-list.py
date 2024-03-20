# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head)
            head = head.next
        tmp = ListNode()
        dummy = tmp
        while lst:
            tmp.next = lst.pop()
            tmp = tmp.next
        tmp.next = None
        return dummy.next