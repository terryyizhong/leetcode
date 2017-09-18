#Divide two integers without using multiplication, division and mod operator.
#If it is overflow, return MAX_INT.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)  # and or 
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor == 0: 
            return 2147483647
        
        ans = 0
        while dividend >= divisor:  # if dividend < divisor, ans will be 0
            tmp = divisor
            step = 1
            while dividend - tmp >= 0:
                dividend -= tmp     # subtract divisor every time and left shift divisor by 1 each time
                ans += step         # when subtract add the step(how many times subtraction of divisor this time)
                step <<= 1
                tmp <<= 1
            
        if not positive:
            ans = -ans
        return min(max(-2147483648, ans), 2147483647) # 2147483647 max_int, prevent overflow
            
