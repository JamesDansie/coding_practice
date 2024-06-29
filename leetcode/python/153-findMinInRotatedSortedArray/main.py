from collections import defaultdict
from typing import List, Optional
import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
    
def main():
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    print(f"output: {solution.findMin(nums)}")

if __name__ == "__main__":
    main()