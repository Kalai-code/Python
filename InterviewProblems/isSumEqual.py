
def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
        alphabets = "abcdefghij"
        firstWord_list = []
        for ch in firstWord:
            firstWord_list.append(alphabets.index(ch))
        secondWord_list = [alphabets.index(i) for i in secondWord]
        targetWord_list = [alphabets.index(j) for j in targetWord]
        firstWord_list = ''.join(map(str,firstWord_list))
        secondWord_list = ''.join(map(str,secondWord_list))
        targetWord_list = ''.join(map(str,targetWord_list))    
        if int(firstWord_list) + int(secondWord_list) == int(targetWord_list):
            return True
        else:
            return False
            
print(isSumEqual(firstWord = "acb", secondWord = "cba", targetWord = "cdb"))