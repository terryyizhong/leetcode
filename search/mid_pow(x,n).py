class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0
        if n < 0:
            return self.myPow(1.0/x, -n)
        if n % 2:
            return x * self.myPow(-x, n-1)
        else:
            return self.myPow(x*x, n/2)     #must reduce n half each time to prevent recursive stack too deep.

# iterative
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0
        if n < 0:
            return self.myPow(1.0/x, -n)
        ans = 1
        while n:
            if n % 2:   # or n & 1
                ans *= x
            x *= x
            n /= 2    # or n >>= 1
        return ans
        
'''
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0){
            return 1.0;
        }
        double t = myPow(x, n/2);
        if (n & 1){
            return n>0 ? x*t*t : t*t*1.0/x;
        }
        else{
            return t*t;
        }
    }
};

class Solution {
public :
    double myPow(double x, int n) {
        unsigned long p; 
        if (n < 0){
            p = -n;
            x = 1.0 / x;
        }
        else{
            p = n;
        }
        double ans = 1;
        while (p){
            if (p & 1){
                ans *= x;
            }
            x *= x;
            p >>= 1;
        }
        return ans;
    }
};
'''

