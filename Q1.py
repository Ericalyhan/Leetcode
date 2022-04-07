class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
          #  print(diff)
            if diff in prevMap:
              #  print([prevMap[diff], i])
                return [prevMap[diff], i]

            prevMap[n] = i
        return
print(4//3)