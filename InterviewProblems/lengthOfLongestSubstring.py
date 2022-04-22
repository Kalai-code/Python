"""
Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s: str) -> int:
        current_str = ""
        out_str = ""
        for ch in s:
            if ch not in current_str:
                current_str = current_str + ch
                #print(current_str)
            else:
                if len(current_str) >= len(out_str):
                    out_str = current_str
                    current_str = ch
        return len(out_str)
"""
            
        
"""
# output : 3
print(lengthOfLongestSubstring("abcabcbb"))
# output: 1
print(lengthOfLongestSubstring("bbbbb"))

# output: 3
print(lengthOfLongestSubstring("pwwkew"))
"""
print(lengthOfLongestSubstring("dvdf"))

print(lengthOfLongestSubstring(" "))
"""
print(lengthOfLongestSubstring("au"))

print(lengthOfLongestSubstring("dvdf"))
"""
