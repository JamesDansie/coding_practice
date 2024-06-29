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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:    
        def util(root: TreeNode):
            nonlocal K
            if root is None:
                return
            left = util(root.left)
            if left is not None:
                return left
            K -= 1
            print(f"k: {K} val: {root.val}")
            if K == 0:
                return root.val
            right = util(root.right)
            if right is not None:
                return right
        K = k
        return util(root)
    
def main():
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(0)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    # root.right.right = TreeNode(7)
    # root.left.right.left = TreeNode(3)
    # root.left.right.right = TreeNode(5)
    
    print(f"output: {solution.kthSmallest(root, 3)}")

if __name__ == "__main__":
    main()