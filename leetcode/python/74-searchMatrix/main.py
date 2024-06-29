from collections import defaultdict
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_matrix(matrix, target):
            for arr in matrix:
                if arr[0] <= target and arr[-1] >= target:
                    return arr
        def run_bs(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = int((left + right) / 2)
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    return True
            return False
        desired_arr = find_matrix(matrix, target)
        if not desired_arr:
            return False
        return run_bs(desired_arr, target)
    
    
    
def main():
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(f"nums: {matrix}, target: {target} ouput: {solution.searchMatrix(matrix, target)}")

if __name__ == "__main__":
    main()