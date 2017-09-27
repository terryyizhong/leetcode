#my slow, brute solution:
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = [""]
        for i in range(2*n):
            tmp = []
            for s in ans:
                if valid(s + "(", n):
                    tmp.append(s + "(")
                if valid(s + ")", n):
                    tmp.append(s + ")")
            ans = tmp
        return ans        
def valid(string, n):
    left = right = 0
    for i in string:
        if i == "(":
            left += 1
        else:
            right += 1
    if left > n or right > left:
        return False
    return True
    
# shorter version of my solution inspired by stephen's solution    
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = [("", n, n)]
        for i in range(2*n):
            tmp = []
            for s in ans:
                for poss in ((s[0] + "(", s[1] - 1, s[2]), (s[0] + ")", s[1], s[2] - 1)):
                    if poss[1] >= 0 and poss[2] >= poss[1]:   # equal still works
                        tmp.append(poss)
            ans = tmp
        return [s[0] for s in ans]
        
        
# stephen's brilliant solution 
def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)
    
# a dp solution:
To generate all n-pair parentheses, we can do the following:

Generate one pair: ()

Generate 0 pair inside, n - 1 afterward: () (...)...

Generate 1 pair inside, n - 2 afterward: (()) (...)...

...

Generate n - 1 pair inside, 0 afterward: ((...))

I bet you see the overlapping subproblems here. Here is the code:

(you could see in the code that x represents one j-pair solution and y represents one (i - j - 1) pair solution, and we are taking into account all possible of combinations of them)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
