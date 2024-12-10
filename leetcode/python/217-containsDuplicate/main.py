from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    dup = set()
    for num in nums:
        if num not in dup:
            dup.add(num)
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