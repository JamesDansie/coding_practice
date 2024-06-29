from collections import defaultdict
from typing import List, Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return f"{self.val}"
    def __repr__(self) -> str:
        return self.__str__

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            left = right = 0
            nonlocal diameter
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            diameter = max(left + right, diameter)
            return max(left, right) + 1
        diameter = 0
        dfs(root)
        return diameter
    
def main():
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    # root.left.right.left = TreeNode(3)
    # root.left.right.right = TreeNode(5)
    
    print(f"output: {solution.diameterOfBinaryTree(root)}")

if __name__ == "__main__":
    main()