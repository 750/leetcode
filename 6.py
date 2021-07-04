class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Typical Pythonic solution
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2]+s[1::2]
        
        # i = 0
        #res = [i for i in s[::2*numRows-2]]
        res = s[::2*numRows-2]
        
        # i = 1...n-2
        for i in range(1,numRows-1):
            j = i
            d = (numRows-1-i)*2
            while j < len(s):
                res += s[j]
                if j+d < len(s):
                    res += s[j+d]
                j += 2*numRows-2
                
        # i = n-1
        res += s[numRows-1::2*numRows-2]
        return res
