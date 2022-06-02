class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        Num_str= str(n)
        sum_num=0
        mul_num=1
        for i in Num_str:
            sum_num +=int(i)
            mul_num *= int(i)
        result = mul_num - sum_num
        return result