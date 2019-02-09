def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    import string
    # s = input("please input the string:")
    #s_raw = input(s)
    s_raw = s[:]
    for i in s_raw:
        if i not in string.letters:
        s_raw.remove(i)
    length = len(s_raw)
    n = 0
    while n <= length/2:
        if s_raw(n) != s_raw(-(n+1)):
            return False
    return True
if __name__ == "__main__":
    isPalindrome("aa")