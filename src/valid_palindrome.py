"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""


class Solution(object):

    def __init__(self):
        self.xjj = "dzx"

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        i = 0
        j = -1
        len0 = len(s)
        print(len0)
        while (i <= len0 / 2) and (j >= -len0 / 2 - 1):
            if s[i].isalnum() != 1:
                i += 1
            elif s[j].isalnum() != 1:
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
                print(i)
                print(j)
            else:
                print("s is not palindrome")
                return False
                break

        if i >= len0 / 2 or j <= -len0 / 2:
            print("s is palindrome")
            return True

my1 = Solution()
print (my1.isPalindrome(""))



