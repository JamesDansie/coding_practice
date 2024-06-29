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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root.val == p.val or root.val == q.val:
            return root
        p_go_left = p.val < root.val
        q_go_left = q.val < root.val
        if p_go_left and q_go_left:
            left = self.lowestCommonAncestor(root.left, p, q)
            if left:
                return left
        elif not p_go_left and not q_go_left:
            right = self.lowestCommonAncestor(root.right, p , q)
            if right:
                return right
        else:
            return root
        
        # """Solution from neetcode"""
        # curr = root
        # while curr:
        #     if p.val > curr.val and q.val > curr.val:
        #         curr = curr.right
        #     elif p.val < curr.val and q.val < curr.val:
        #         curr = curr.left
        #     else:
        #         return curr
    
def main():
    solution = Solution()
    root = TreeNode(6)
    node_2 = root.left = TreeNode(2)
    node_8 = root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    node_4 = root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    
    print(f"output: {solution.lowestCommonAncestor(root, node_2, node_4)}")

if __name__ == "__main__":
    main()