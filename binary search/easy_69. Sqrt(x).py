#Implement int sqrt(int x).

#Compute and return the square root of x.
# eg. return 1 if x == 2

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x == 0 or x == 1:
            return x
        low, high = 1, x / 2
        while low < high:
            mid = (low + high + 1) / 2
            pow2 = mid * mid
            if pow2 == x:
                return mid
            elif pow2 < x:
                low = mid
            else:
                high = mid - 1
        return high 
        
