import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        print(s)
        lens = len(s)
        j=0
        for j in range(round(lens/2)):
            if (s[j].lower() != s[lens-j-1].lower()):
                print(f'{s[j].lower()}, {s[lens-j-1].lower()}, not a palendrome')
                return False
        print('its a palindrome')
        return True

sol = Solution()
str1 = "A man, a plan, a canal: Panama"
str2 = "race a car"
sol.isPalindrome(str1)
sol.isPalindrome(str2)
str3="abcdef _ ghij #$ ihg** fedcba"
print(str3)
sol.isPalindrome(str3)
