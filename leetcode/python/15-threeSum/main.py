from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        pivot = 0
        while pivot < len(nums) and nums[pivot] < 1:
            left = pivot + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[pivot] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0 :
                    right -= 1
                else:
                    res.append([nums[pivot], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < (len(nums) - 1):
                        left += 1
            pivot += 1
            while pivot < (len(nums) - 1) and nums[pivot] == nums[pivot - 1]:
                pivot += 1
        return res
    
def main():
    solution = Solution()
    nums = [-1,0,1,2,-1,-1,-4]
    print(f"output: {solution.threeSum(nums)}")
    nums1 = [0, 0, 0]
    print(f"output: {solution.threeSum(nums1)}")


if __name__ == "__main__":
    main()