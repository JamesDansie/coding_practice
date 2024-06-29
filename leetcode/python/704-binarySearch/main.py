from collections import defaultdict
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
    
    
def main():
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = -1
    print(f"nums: {nums}, target: {target} ouput: {solution.search(nums, target)}")

if __name__ == "__main__":
    main()