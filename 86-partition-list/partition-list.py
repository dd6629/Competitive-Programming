# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        stack1 = []
        stack2 = []
        tmp = head
        while head:
            y = head.val
            if y<x:
                stack1.append(y)
            else:
                stack2.append(y)
            head = head.next
        tmp1 = tmp
        head = tmp

        i = 0
        l = len(stack1)
        while i < l:
            tmp = ListNode()
            tmp.val = stack1[i]
            head.next = tmp
            head = head.next
            i+=1
        i = 0
        l = len(stack2)
        while i < l:
            tmp = ListNode()
            tmp.val = stack2[i]
            head.next = tmp
            head = head.next
            i+=1
        return tmp1.next