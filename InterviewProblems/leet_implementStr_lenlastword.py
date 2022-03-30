def lengthOfLastWord(s: str) -> int:
    wordlist = []
    wordlist = s.split()
    return len(wordlist[-1])
     
     
#Test Case 1 - Output : 5
print(lengthOfLastWord("Hello World"))

def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
        
# Test Case 1 - Output : 2
print(strStr("hello","ll"))