# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def leafnode(root, path):
            if not root.left and not root.right:
                res.append(path+[root.val])
                return
            if root.left:
                leafnode(root.left,path+[root.val])
            if root.right:
                leafnode(root.right,path+[root.val])
        leafnode(root, [])
        return ("->".join(map(str,i)) for i in res)

