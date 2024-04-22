# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not preorder:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[0])
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        head = TreeNode(preorder[0])
        mid = preorder.index(postorder[-2])
        postorderLeft = postorder[0:mid-1]
        postorderRight = postorder[mid-1:-1]
        preorderLeft = preorder[1:mid]
        preorderRight = preorder[mid:]
        head.left = self.constructFromPrePost(preorderLeft,postorderLeft)
        head.right = self.constructFromPrePost(preorderRight,postorderRight)
        return head