# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def list_to_array(head):
            array = []
            while head:
                array.append(head.val)
                head = head.next
            return array
        def build_BST(left, right):
            if left > right:
                return None 
            mid = (left + right) // 2
            node = TreeNode(array[mid])
            node.left = build_BST(left, mid - 1)
            node.right = build_BST(mid + 1, right) 
            return node
        if not head:
            return None
        
        array = list_to_array(head)
        return build_BST(0, len(array) - 1)
