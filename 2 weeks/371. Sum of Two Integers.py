'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF  
        mask = 0xFFFFFFFF   # use to get 32-bit version of python int
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask  # get 32-bit version of add and carry
        return a if a <= MAX else ~(a ^ mask)     #if smaller than 32-bit max, means positive. else negative: use ~(a ^ mask)                                                       get 32-bit negative int
            
