
def solution(s):
    N = len(s)
    if N == 0: return ''
    if N == 1: return s
    if N == 2:
        if s[0] != s[1]: return s[0]
        else: return s

    dp = [[0] * N for _ in range(N)]

    longest_ss = -1
    longest_ss_val = ''

    for i in range(N):
        # for length 1
        dp[i][i] = 1
        # for length 2
        if i+1 >= N: continue
        if (s[i] == s[i+1]):
            dp[i][i+1] = 1

    offset = 2
    while offset < N:
        for i in range(N):
            j = i + offset
            if j >= N: break
            if s[i] == s[j]:
                if dp[i+1][j-1] == 1:
                    dp[i][j] = 1
        offset += 1

    for i in range(N):
        for j in range(i, N):
            if (dp[i][j]) and (longest_ss < (j-i+1)):
                longest_ss = j-i+1
                longest_ss_val = s[i:j+1]

    return longest_ss_val

solution('babad')
