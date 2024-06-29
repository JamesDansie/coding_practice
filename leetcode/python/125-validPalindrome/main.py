

def isPalindrome(s: str) -> bool:
    simple_str = ""
    for char in s:
        if char.isalpha():
            simple_str += char.lower()
        elif char.isnumeric():
            simple_str += char
    for i in range(int(len(simple_str)/2)):
        if simple_str[i] != simple_str[-(i + 1)]:
            return False
    return True
    
def main():
    # s = "A man, a plan, a canal: Panama"
    s = "0P"
    print(f"Is {s} a palindrome? {isPalindrome(s)}")

if __name__ == "__main__":
    main()