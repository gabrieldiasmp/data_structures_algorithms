from subsequence import isSubsequence

def test_panama_string(s="abc", t="ahcgdb"):
    assert isSubsequence(s, t) == False

def test_panama_string_with_modifications(s="abc", t="ahbgdc"):
    assert isSubsequence(s, t) == True

def test_empty_string(s="axc", t="ahcgdb"):
    assert isSubsequence(s, t) == False
