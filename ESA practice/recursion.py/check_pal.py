def is_palindrome(s):
    if len(s) <= 1:      # Base case
        return True
    if s[0] != s[-1]:    # Characters don't match
        return False
    return is_palindrome(s[1:-1])  # Recursive call