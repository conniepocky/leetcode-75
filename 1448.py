# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, currentMax):
            nonlocal count
            
            if not node:
                return

            if node.val >= currentMax:
                count += 1
                currentMax = node.val

            dfs(node.left, currentMax)
            dfs(node.right, currentMax)

        dfs(root, root.val)

        return count
