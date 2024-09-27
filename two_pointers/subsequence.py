def isSubsequence(s, t):
    sp = tp = 0

    while sp < len(s) and tp < len(t):
        print(f"lower: {sp} | upper: {tp}")
        if s[sp] == t[tp]:
            sp += 1
        tp += 1
            

    return sp == len(s)

if __name__ == "__main__":
    s = "abc"
    t = "ahcgdb"
    
    print(isSubsequence(s, t))