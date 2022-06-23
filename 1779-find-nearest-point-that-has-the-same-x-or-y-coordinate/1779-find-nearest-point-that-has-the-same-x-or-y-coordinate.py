class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        ans = -1
        minDist = float('inf')
        for i, (a, b) in enumerate(points):
            if a ==x or b==y:
                distance = abs(a-x)+abs(b-y)
                if distance < minDist:
                    minDist=distance
                    ans = i
        return ans
            
