from collections import defaultdict
from typing import List, Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check_same_tree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not root and not sub_root:
            return True
        if not root or not sub_root:
            return False
        if root.val != sub_root.val:
            return False
        return self.check_same_tree(root.left, sub_root.left) and self.check_same_tree(root.right, sub_root.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        same = False
        if root.val == subRoot.val:
            same = self.check_same_tree(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return same or left or right
    
def main():
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)
    sub_root = TreeNode(4)
    sub_root.left = TreeNode(1)
    sub_root.right = TreeNode(2)
    print(f"output: {solution.isSubtree(root, sub_root)}")

if __name__ == "__main__":
    main()