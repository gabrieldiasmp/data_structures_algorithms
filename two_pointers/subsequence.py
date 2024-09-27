def isSubsequence(s, t):
    sp = tp = 0

    while sp <= len(s) -1 and tp <= len(t) - 1:
        print(f"lower: {sp} | upper: {tp}")
        if s[sp] == t[tp]:
            sp += 1
            tp += 1
        else:
            tp += 1
            

    return sp == len(s)

if __name__ == "__main__":
    s = "abc"
    t = "ahcgdb"
    
    print(isSubsequence(s, t))