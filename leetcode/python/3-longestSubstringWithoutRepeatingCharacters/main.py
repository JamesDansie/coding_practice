# def lengthOfLongestSubstring( s: str) -> int:
#     if s == "":
#         return 0
    
#     if len(s) == 1:
#         return 1
#     res = [0] * len(s)
#     for index in range(len(s)-1):
#         unique_chars = set()
#         for sub_index, char in enumerate(s[index:]):
#             print(f"index: {index} char: {char} s[index:] {s[index:]} res: {res} unique: {unique_chars} sub_index:{sub_index}")
#             if char in unique_chars:
#                 res[index] = len(unique_chars)
#                 break
#             elif sub_index == len(s[index:]) - 1:
#                 res[index] = sub_index + 1
#             else:
#                 unique_chars.add(char)
#     print(f"final res: {res}")
#     return max(res)
def lengthOfLongestSubstring( s: str) -> int:
    unique_chars = set()
    ans = 0
    current_count = 0
    left = right = 0
    while right < len(s):
        if s[right] not in unique_chars:
            unique_chars.add(s[right])
            current_count += 1
            right += 1
        else:
            unique_chars.remove(s[left])
            current_count -= 1
            left += 1
        ans = max(ans, current_count)
    return ans


def main():
    blah = "abcabcbb"
    print(f"Longest sequence of {blah}: {lengthOfLongestSubstring(blah)}")
    foo = "pwwkew"
    print(f"Longest sequence of {foo}: {lengthOfLongestSubstring(foo)}")

if __name__ == "__main__":
    main()