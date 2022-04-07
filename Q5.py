class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_0 = 0
        middle = 0
        for i in range(1,len(s)-1):
            len1 = self.length_Calc(s, i, i)
            len2 = self.length_Calc(s, i, i + 1)
            len3 = len1 if (len1 > len2) else len2
            if len3 > len_0:
                len_0 = len3
                middle = i

        left = int(middle - (len_0 - 1) / 2)
        right = int(middle + (len_0 + 1) / 2)
        print(s[left:right])

    def length_Calc (self,s, left, right):
        if len(s)==0 or left > right:
            return 0
        while left>=0 and right< len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return int( right - left - 1)
