class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list=[]
        for i,j in enumerate(s):
            if j in list:
                break
            list.append(j)
        return len(list)