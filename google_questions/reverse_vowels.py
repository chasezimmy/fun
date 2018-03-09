# Reverse Vowels in a string

class Solution:
    def reverse_vowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = ['a','e','i','o','u']
        k = len(s)
        reverse = list(s)
        i,j = 0, k-1

        for _ in s:
            cur, rev = s[i].lower(), s[j].lower()

            if cur not in VOWELS:
                i += 1

            if rev not in VOWELS:
                j -= 1

            if cur in VOWELS and rev in VOWELS:
                reverse[i], reverse[j] = reverse[j], reverse[i]
                i, j = i+1, j-1

            if i == j or i > j:
                break
                
        return ''.join(reverse)

    def fast_reverse_vowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = "aeiouAEIOU"
        k = len(s)
        s = list(s)
        i,j = 0, k-1

        for _ in s:
            cur, rev = s[i], s[j]

            if cur not in VOWELS:
                i += 1
                continue

            if rev not in VOWELS:
                j -= 1
                continue

            if i == j or i > j:
                break

            s[i], s[j] = s[j], s[i]
            i, j = i+1, j-1
                
        return ''.join(s)

    def lambda_reverse_vowels(self, s):
        import re
        vowels = re.findall('(?i)[aeiou]', s)
        print(vowels)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)        

sol = Solution()
str = "Slap-dab set-up, Mistress Ann asserts, imputes bad pals."
print(sol.lambda_reverse_vowels(str))
