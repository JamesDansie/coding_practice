from typing import List
import heapq
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # freq = {}
    # ans = []
    # for num in nums:
    #     freq[num] = freq.get(num, 0) + 1
    # for _ in range(k):
    #     max_value = max(freq.values())
    #     for key in freq.keys():
    #         if freq[key] == max_value:
    #             ans.append(key)
    #             freq.pop(key)
    #             break
    # return ans
    if len(nums) == k:
        return nums
    
    # turns this [1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4] 
    # into this  Counter({4: 6, 1: 4, 2: 2, 3: 1}) 
    count = Counter(nums)
    # return count.most_common(k)
    return heapq.nlargest(k, count.keys(), key=count.get)
    


def main():
    nums = [1,1,1,1,2,2,3,4,4,4,4,4,4]
    k = 2
    print(f"top K Freq nums: {nums} k: {k} result: {topKFrequent(nums, k)}")

if __name__ == "__main__":
    main()