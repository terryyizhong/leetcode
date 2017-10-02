'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# my worst, slowest ac solution

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans, old_ans = [], None
        while ans != old_ans:
            old_ans, ans = ans, []
            for i in intervals:
                merge = False
                for mi in ans:
                    if  mi.start <= i.start <= mi.end:
                        mi.end = max(mi.end, i.end)
                        merge = True
                    if mi.start <= i.end <= mi.end:
                        mi.start = min(mi.start, i.start)
                        merge = True
                    if mi.start <= i.start and mi.end >= i.end:
                        merge = True
                    if mi.start >= i.start an/d mi.end <= i.end:
                        mi.start, mi.end = i.start, i.end
                        merge = True
                if not merge:
                    ans.append(i)
            intervals = ans
        return ans
        
# stephan's concise solution use sort by intervals.start (optimal)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        for i in sorted(intervals, key = lambda x: x.start):
            if ans and i.start <= ans[-1].end:
                ans[-1].end = max(ans[-1].end, i.end)
            else:
                ans.append(i)
        return ans
                
