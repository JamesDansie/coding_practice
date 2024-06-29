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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [0, True]
            res_left = dfs(root.left)
            res_right = dfs(root.right)
            height_delta = abs(res_left[0] - res_right[0])
            height = 1 + max(res_left[0], res_right[0])
            if not res_left[1] or not res_right[1] or height_delta > 1:
                return [height, False]
            else:
                return [height, True]
        res = dfs(root)
        return res[1]
    
def main():
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    # root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    
    print(f"output: {solution.isBalanced(root)}")

if __name__ == "__main__":
    main()