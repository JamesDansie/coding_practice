from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack(first, curr):
        if k <= len(curr):
            print(f"BC curr: {curr} k: {k} len: {len(curr)}")
            res.append(curr.copy())
            return
        for i in range(first, n):
            # breakpoint()
            curr.append(nums[i])
            print(f"for curr: {curr}")
            backtrack(i + 1, curr)
            curr.pop()

    
    res = []
    n = len(nums)
    for k in range(n + 1):
        backtrack(0, [])
    return res

def subsets_correct(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)
    dfs(0)
    return res

def main():
    nums = [1,2,3]
    # print(subsets(nums))
    print(subsets_correct(nums))

if __name__ == "__main__":
    main()