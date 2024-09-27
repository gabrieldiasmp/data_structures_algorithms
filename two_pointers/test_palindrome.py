from palindrome import isPalindrome

def test_panama_string(string="A man, a plan, a canal: Panama"):
    assert isPalindrome(string) == True

def test_panama_string_with_modifications(string="A man, a plan, a tst canal: Panama"):
    assert isPalindrome(string) == False

def test_empty_string(string=" "):
    assert isPalindrome(string) == True

