class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        product = reduce((lambda x, y: x * y), nums)
        if product > 0:
            return 1
        elif product < 0:
            return -1
        return 0