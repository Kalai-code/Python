

def longestPalindrome(s: str) -> str:
        inputstr = ""
        longestPalindrome = ""
        for i in range(len(s)):
            ch_count = s.count(s[i])
            if ch_count > 1:
                inputstr = inputstr + s[i]
                print(inputstr)
                if len(inputstr) > 1 and inputstr == inputstr[::-1]:
                    if len(inputstr) > len(longestPalindrome):
                        longestPalindrome = inputstr
        return longestPalindrome
        
#print(longestPalindrome("babad"))

#print(longestPalindrome("cbbd"))

print(longestPalindrome("bdabad"))