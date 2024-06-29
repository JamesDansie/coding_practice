def characterReplacement(s: str, k: int) -> int:
    ans = left = right = 0
    char_count = {}
    while right < len(s):
        window_length = right - left + 1
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_char = max(char_count.values())
        # print(f"right: {right} left: {left}: window_length: {window_length} max_char: {max_char} char_count: {char_count} ")
        while window_length - max_char > k:
            char_count[s[left]] -= 1
            left += 1
            window_length = right - left + 1
            max_char = max(char_count.values())

        ans = max(ans, window_length)
        right += 1
        # while right - left + 1 - max(char_count.values()) > k:
        #     char_count[s[left]] = char_count[s[left]] - 1
        #     left += 1
        # ans = max(ans, right - left + 1)
        # right += 1
    return ans


def main():
    blah = "ABAB"
    print(f"Longest sequence of {blah}: {characterReplacement(blah, 2)}")
    blah1 = "AABABBA"
    print(f"Longest sequence of {blah1}: {characterReplacement(blah1, 1)}")

if __name__ == "__main__":
    main()