from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    hash = {}
    for num in nums:
        res = hash.get(num)
        if not res:
            hash[num] = 1
        else:
            return True
        
    return False


def main():
    nums = [1,2,3,4]
    nums_fail = [1,2,1]
    print(containsDuplicate(nums))
    print(containsDuplicate(nums_fail))

if __name__ == "__main__":
    main()