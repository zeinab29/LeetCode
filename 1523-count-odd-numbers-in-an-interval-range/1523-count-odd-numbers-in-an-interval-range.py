class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        if (high-low+1)%2 ==0 or high%2==0 :
            return((high-low+1)//2)
        else:
            return((high-low+1)//2 +1)
            