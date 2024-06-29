from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for index, num in enumerate(nums):
            diff = target - num
            if num in diffs:
                return [index, diffs[num]]
            else:
                diffs[diff] = index
    
def main():
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    print(f"output: {solution.twoSum(nums, target)}")

if __name__ == "__main__":
    main()