from typing import List, Optional

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
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, max_int: int) -> int:
            if not root:
                return 0
            if root.val >= max_int:
                count = 1
            else:
                count = 0
            new_max = max(max_int, root.val)
            return dfs(root.left, new_max) + dfs(root.right, new_max) + count
        return dfs(root, root.val)
    
def main():
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.left.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    root.right.left = TreeNode(1)
    # root.left.right.left = TreeNode(3)
    # root.left.right.right = TreeNode(5)
    
    print(f"output: {solution.goodNodes(root)}")

if __name__ == "__main__":
    main()