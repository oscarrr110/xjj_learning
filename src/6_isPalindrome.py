"""
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <= 0:
            #print("wrong1")
            return False
        else:
            import math
            num = 0
            x0 = x
            x1 = x
            x_rev = 0
            #求x的位数
            while x0/10 != 0:
                x0 = x0//10
                num += 1
            i = 1
            while i <= num:
                tmp = math.pow(10, num-i)
                x_rev += x1 % 10 * tmp
                x1 = x1//10
                i += 1
            if x_rev == x:
                #print("right")
                return True
            else:
                #print("wrong2")
                return False


my1 = Solution()
my1.isPalindrome(1221)
