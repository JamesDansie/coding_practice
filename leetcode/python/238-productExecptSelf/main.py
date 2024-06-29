from typing import List, Optional

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # multiply by inverse instead of using division
        # ans = []
        # num_zeros = nums.count(0)
        # if num_zeros >= 2:
        #     return [0 for _ in nums]
        # elif num_zeros == 1:
        #     zero_pos = nums.index(0)
        #     ans = [0 for _ in nums]
        #     total = 1
        #     for num in nums:
        #         if num == 0:
        #             continue
        #         total *= num
        #     ans[zero_pos] = total
        #     return ans
        # else:
        #     total = 1
        #     for num in nums:
        #         total *= num
        #     for num in nums:
        #         ans.append(int(total*(1/num)))
        #     return ans
        res = [1 for _ in nums]
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res

def main():
    nums = nums = [1,2,3,4]
    solution = Solution()
    print(f"output: {solution.productExceptSelf(nums)}")

if __name__ == "__main__":
    main()