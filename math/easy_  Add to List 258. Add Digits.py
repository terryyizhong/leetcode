'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''
###briliant O(1):
'''
Digital Root
this method depends on the truth:

N=(a[0] * 1 + a[1] * 10 + ...a[n] * 10 ^n),and a[0]...a[n] are all between [0,9]

we set M = a[0] + a[1] + ..a[n]

and another truth is that:

1 % 9 = 1

10 % 9 = 1

100 % 9 = 1

so N % 9 = a[0] + a[1] + ..a[n]

means N % 9 = M

so N = M (% 9)

as 9 % 9 = 0,so we can make (n - 1) % 9 + 1 to help us solve the problem when n is 9.as N is 9, ( 9 - 1) % 9 + 1 = 9

'''
##########bravo!!!!
    def addDigits(self, num):
        return (num - 1) % 9 + 1 if num else 0

#normal way: O(n) n is the number of digits of the number
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0
        while num / 10:
            num = self.add_all(num)
        return num
        
        
    def add_all(self, num):
        if not num:
            return 0
        ans = 0
        while num:
            ans += num % 10
            num = num / 10
        return ans
