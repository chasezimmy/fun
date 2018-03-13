class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        
        last = 0
        total = 0
        
        for c in list(s)[::-1]:
            if value[c] >= last:
                total += value[c]
            else:
                total -= value[c]
            last = value[c]
        
        return total