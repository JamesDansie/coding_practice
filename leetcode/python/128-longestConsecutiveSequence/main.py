from typing import List, Optional

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in num_set:
                seq_length = 0
                curr = num
                while curr in num_set:
                    seq_length += 1
                    curr += 1
                ans = max(ans, seq_length)
        return ans

def main():
    # nums = []
    nums = [100,4,200,1,3,2]
    solution = Solution()
    print(f"output: {solution.longestConsecutive(nums)}")

if __name__ == "__main__":
    main()