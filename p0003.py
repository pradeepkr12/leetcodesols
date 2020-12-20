def solution(s):
    if len(s) == 0: return 0
    if len(s) == 1: return 1
    longest_ss = 0
    d = {}
    ss = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c in d:
            longest_ss = max(ss, longest_ss)
            # prev_i = i
            i = d[c] + 1 # go back,start parsing again
            d = {}
            ss = 0
            # ss = 1
            # d[c] = prev_i
            # print ("start", prev_i, c, i, ss, longest_ss, d)
            continue
        ss += 1
        d[c] = i
        i += 1
        # print ("end", ss, longest_ss, d)
    longest_ss = max(ss, longest_ss)
    return longest_ss
