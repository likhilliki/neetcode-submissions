# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}

        def helper(preorder,inorder):
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])
            mid = idx_map[preorder[0]] - idx_map[inorder[0]]
            root.left = helper(preorder[1:mid + 1],inorder[:mid])
            root.right = helper(preorder[mid + 1:],inorder[mid + 1:])
            return root

        return helper(preorder,inorder)