from typing import List

def solution(values, run_length):
    # Algo: Start at the back of the array and keep a run_count. By starting at the end we don't 
    # need to keep track of the starting index of the run. If the next value is within +/- 1
    # of the current value then run_count++. Once run_count >= run_length, then if the next value
    # is within +/- 1 then we add that index to the results. Otherwise reset run_count to 0.
    # The space complexity would O(1) since there's no extra data structure (unless you include the
    # result array in which case it would O(n)).
    # The time complexity would be O(n) since we go through the array only once.


    if run_length < 1 or len(values) < 2:
        return []
    # run length = 1 is a weird case because then we don't care if the previous value was
    # increasing or decreasing.
    if run_length == 1:
        res = []
        for i in range(len(values) - 2, -1, -1):
            diff = values[i] - values[i + 1]
            if abs(diff) == 1:
                res.append(i)
        return res
    res = []
    run_count = 0
    diff_prev = values[-2] - values[-1]
    if abs(diff_prev) == 1:
        run_count = 1
    for i in range(len(values) - 3, -1, -1):
        diff_curr = values[i] - values[i + 1]
        if abs(diff_curr) == 1 and diff_prev == diff_curr:
            run_count += 1
            if run_count >= run_length - 1:
                res.insert(0, i)
        elif abs(diff_curr) == 1:
            run_count = 1
        else:
            run_count = 0
        diff_prev = diff_curr
    return res

def main():
    candidates = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
    # candidates = [1, 2, 3, 1]
    run_length = 3
    print(f"Output: {solution(candidates, run_length)}")

if __name__ == "__main__":
    main()