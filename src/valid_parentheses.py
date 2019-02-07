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
        list1 = ["(", "[", "{"]
        list2 = [")", "]", "}"]
        map = {'(': ')', '[': ']', '{': '}'}
        i = 0
        list_new = []
        while i < len_s:
            if list_s[i] in list1:
                list_new.append(list_s[i])
            elif list_s[i] in list2:
                if len(list_new) == 0:
                    return False
                elif map[list_new[-1]] == list_s[i]:
                    list_new.pop()
                else:
                    return False

            i += 1
        if i >= len_s-1 and list_new == []:
            return True
        else:
            return False

my1 = Solution()
print(my1.isValid("["))


