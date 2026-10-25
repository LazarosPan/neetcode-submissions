"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Given a meetings schedule with time intervals, find if it is possible to
        add all meetings in the schedule, only if they dont overlap with each other

        Args:
            intervals: meeting time interval objects consisting of start and end times
        
        Returns:
            True if all meetings can be added without overlaps
            False if meetings overlap
        """
        if not intervals:
            return True

        # (0, 30), (5, 10), (15, 20)
        # 0, 5, 10, 15, 20, 30

        intervals.sort(key = lambda meeting : meeting.start)

        previous = None

        for meeting in intervals: # meeting = (start, end)
            if previous is not None:
                if previous.end > meeting.start:
                    return False
            
            previous = meeting
            
        return True
