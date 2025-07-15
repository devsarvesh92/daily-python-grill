def valid_palindrome(*, s: str) -> bool:
    clean_str = "".join([c for c in s.lower() if c.isalnum()])

    i, j = 0, len(clean_str) - 1

    while i < j:
        if clean_str[i] != clean_str[j]:
            return False
        i += 1
        j -= 1

    return True
