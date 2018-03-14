class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        length_b = len(B)
        
        for i in range(length_b):
            if A == B[i::] + B[:i]:
                return True
            
        return False

        