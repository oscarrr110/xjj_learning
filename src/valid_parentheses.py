"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""


class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_s = list(s)
        len_s = len(list_s)
        list1 = ["(", ")"]
        list2 = ["[", "]"]
        list3 = ["{", "}"]
        i = 0
        while i < len_s/2:
            if list_s[i] == list1[0] and list_s[len_s-1-i] == list1[1]:
                i += 1
            elif list_s[i] == list2[0] and list_s[len_s-1-i] == list2[1]:
                i += 1
            elif list_s[i] == list3[0] and list_s[len_s-1-i] == list3[1]:
                i += 1
            else:
                print("wrong")
                return False
        if i >= len_s/2:
            print("right")
            return True


my1 = Solution()
my1.isValid("({[}])")


