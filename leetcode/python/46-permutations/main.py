from typing import List

class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     # neet code sol
    #     res = []
    #     if len(nums) == 1:
    #         return [nums.copy()]
        
    #     for i in range(len(nums)):
    #         num = nums.pop(0)
    #         perms = self.permute(nums)

    #         for perm in perms:
    #             # breakpoint()
    #             perm.append(num)

    #         res.extend(perms)
    #         nums.append(num)

    #     return res
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(res: List[List[int]], cur: List[int], nums: List[int]):
            # solution from: https://www.youtube.com/watch?v=H232aocj7bQ
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for num in nums:
                if num in cur:
                    continue
                cur.append(num)
                backtrack(res, cur, nums)
                cur.pop()
        
        res = []
        backtrack(res, [], nums)
        return res

def main():
    candidates = [1, 2, 3] 
    solution = Solution()
    print(f"Output: {solution.permute(candidates)}")

if __name__ == "__main__":
    main()