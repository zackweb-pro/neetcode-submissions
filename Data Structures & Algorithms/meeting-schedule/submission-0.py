"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i, l1 in enumerate(intervals):
            for j, l2 in enumerate(intervals):
                if i>j and l2.start <= l1.start < l2.end:
                    return False
        return True