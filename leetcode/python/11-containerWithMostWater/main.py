from typing import List, Optional

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = left = 0
        right = len(height) - 1
        while left < right:
            h_l = height[left]
            h_r = height[right]
            area = min(h_l, h_r) * (right - left)
            ans = max(ans, area)
            if h_l < h_r:
                left += 1
            else:
                right -= 1
        return ans

def main():
    # nums = []
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(f"output: {solution.maxArea(height)}")

if __name__ == "__main__":
    main()