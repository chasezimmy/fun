class Solution:
    """ Naive make int a string """
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        length = len(string)
        is_even = length%2
        if length == 1:
            return True
        half = length//2
        return string[:half] == string[half+is_even:][::-1]


    def isPalindrome_string(self, x):
        x = str(x)
        return x[0::]==x[::-1]


class Solution:
    """ No extra space, no integer overflow """
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        div = 1
        
        while x//div >= 10:
            div *= 10
        
        while x != 0:
            l = x // div
            r = x % 10
            if l != r:
                return False
            
            x = (x % div) // 10
            div //= 100
        
        return True


class Solution:
    """ No extra space, but possible integer overflow """
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        copy, reverse = x, 0
        
        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10
            print(reverse)
            
        return x == reverse
