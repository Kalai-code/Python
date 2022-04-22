"""
Given a string s, find the length of the longest substring without repeating characters.
"""
def lengthOfLongestSubstring(s: str) -> int:
        outStr = ""
        strLength = 0
        i = 0
        if len(s) > 1:
            while i < len(s):
                if i < len(s) - 1:
                    if s[i] == s[i+1]:
                        i = i + 1
                        if s[i] not in outStr:
                            outStr = outStr + s[i]
                    else:
                        if s[i] not in outStr:
                            outStr = outStr + s[i]
                        else:
                            outStr = ""
                            outStr = outStr + s[i]
                        i = i + 1
            return len(outStr)
        else:
            return len(s)

print(lengthOfLongestSubstring("abcabcbb"))

print(lengthOfLongestSubstring("bbbbb"))
"""
print(lengthOfLongestSubstring("pwwkew"))

print(lengthOfLongestSubstring(" "))

print(lengthOfLongestSubstring("au"))

print(lengthOfLongestSubstring("dvdf"))
"""
