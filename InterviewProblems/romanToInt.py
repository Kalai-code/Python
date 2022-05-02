def romanToInt(s: str) -> int:
        intNum = 0
        while len(s) > 0:
            if 'M' in s:
                if 'CM' in s:
                    intNum+=900
                    s = s[s.index('CM') + 2:]
                else:
                    intNum+=1000
                    s = s[s.index('M') + 1:]
                print(s)
            elif 'D' in s:
                intNum+=500
                s = s[s.index('D') + 1:]
            elif 'C' in s:
                print(s)
                if 'CM' in s:
                    print(s)
                    intNum+=900
                    s = s[s.index('CM') + 2:]
                elif 'CD' in s:
                    intNum+=400
                    s = s[s.index('CD') + 2:]
                else:
                    intNum+=100
                    s = s[s.index('C') + 1:]
                print(s)
            elif 'L' in s:
                intNum+=50
                s = s[s.index('L') + 1:]            
            elif 'X' in s:
                if 'XL' in s:
                    intNum+=40
                    s = s[s.index('XL') + 2:]
                elif 'XC' in s:
                    intNum+=90
                    s = s[s.index('XC') + 2:]
                else:
                    intNum+=10
                    s = s[s.index('X') + 1:]
            elif 'IX' in s:
                intNum+=9
                s = s[s.index('IX') + 2:]
            elif 'V' in s:
                intNum+=5
                s = s[s.index('V') + 1:]
            elif 'IV' in s:
                intNum+=4
                s = s[s.index('IV') + 2:]
            elif 'III' in s:
                intNum+=3
                s = s[s.index('III') + 3:]
            elif'II' in s:
                intNum+=2
                s = s[s.index('II') + 2:]
            elif 'I' in s:
                intNum+=1
                s = s[s.index('I') + 1:]
        return intNum

print(romanToInt('MCMXCIV'))