from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    # for index_1 in range(len(numbers)):
    #     for index_2 in range(index_1 + 1, len(numbers)):
    #         if numbers[index_1] + numbers[index_2] == target:
    #             return [index_1 + 1, index_2 + 1]
    l, r = 0, len(numbers) - 1
    while True:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l + 1, r + 1]
        elif sum > target:
            r -= 1
        else:
            l += 1
    
    
def main():
    numbers = [2,3,4]
    target = 6
    print(f"Does {numbers} sum to {target}? {twoSum(numbers, target)}")

if __name__ == "__main__":
    main()