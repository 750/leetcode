class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n) linear solution: Manacher's algorithm

        s = "!"+"!".join(s)+"!"
        deltas = [-1 for i in range(len(s))]
        deltas[0] = 0
        biggest_center = 0
        res = 0
        for center in range(0, len(s)):
            # mirror
            mirror = 2*biggest_center-center
            
            start = 0
            if center <= biggest_center+deltas[biggest_center]:
                start = min(deltas[mirror], biggest_center+deltas[biggest_center]-center)
            
            while center-start >= 0 and center+start < len(s):
                if s[center+start] == s[center-start]:
                    start+=1
                else:
                    break
            
            start -= 1
            if center+start >= biggest_center+deltas[biggest_center]:
                biggest_center = center
            
            if start > deltas[res]:
                res = center
            deltas[center] = start
            
        return ''.join([i for i in s[res-deltas[res]:res+deltas[res]+1] if i != "!"])
