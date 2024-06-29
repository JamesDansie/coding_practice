

def alpha_numeric(input: str) -> bool:
    if not isinstance(input, str) or not input:
        return False
    is_alpha_numeric = True
    for char in input:
        if not char.isalpha() and not char.isnumeric():
            is_alpha_numeric = False
    return is_alpha_numeric

def main():
    print(alpha_numeric("a"))


if __name__ == "__main__":
    main()