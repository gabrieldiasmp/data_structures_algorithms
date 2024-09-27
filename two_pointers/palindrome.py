def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    s_lower = s.lower()
    s_clean = [letter for letter in s_lower if letter.isalnum()]

    print(f"--------- CLEAN STRING: {s_clean}")
    size_string = len(s_clean)

    if size_string == 0:
        return True

    size_string -= 1
    upper = size_string
    lower = 0

    while upper != lower:
        print(f"lower: {lower} | upper: {upper}")
        print(f"lower: {s_clean[lower]} | upper: {s_clean[upper]}")
        if s_clean[lower] == s_clean[upper]:
            upper -= 1
            lower += 1
        else:
            return False

    answer = True
    
    return answer

if __name__ == "__main__":
    # s = "A man, a plan, a canal: Panama" #### True
    # s = " " #### True
    s = "A man, a plan, a canal tst: Panama" #### False

    print(isPalindrome(s))