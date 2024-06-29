from typing import List, Optional

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
        
    
def main():
    solution = Solution()
    # nums = [2,5,9,6,9,3,8,9,7,1]
    nums = [1,3,4,2,2]
    print(f"{solution.findDuplicate(nums)}")

if __name__ == "__main__":
    main()