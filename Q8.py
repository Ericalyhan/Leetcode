class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        rev = 0
        for i in range(len(s)):
            if s[i] == '+':
                y = True
            if s[i] == '-':
                y = False
            if s[i].isnumeric():
                num = int(s[i])
                rev = rev * 10 + num
        return rev if y else  -rev
