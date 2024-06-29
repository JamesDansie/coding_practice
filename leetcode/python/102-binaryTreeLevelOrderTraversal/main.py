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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        queue.append(root)

        while queue:
            length = len(queue)
            sub_res = []
            for i in range(length):
                curr_node = queue.pop(0)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                sub_res.append(curr_node.val)
            res.append(sub_res)
        return res
    
def main():
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    # root.left.left = TreeNode(0)
    # root.left.right = TreeNode(4)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # root.left.right.left = TreeNode(3)
    # root.left.right.right = TreeNode(5)
    
    print(f"output: {solution.levelOrder(root)}")

if __name__ == "__main__":
    main()