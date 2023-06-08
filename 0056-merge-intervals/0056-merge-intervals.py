class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        noIntervals = [intervals[0]]
        
        for idx in range(1, len(intervals)):
            left = noIntervals[-1]
            right = intervals[idx]
            if(left[1] < right[0]):
                noIntervals.append(right)
                continue
            if(left[1] < right[1]):
                noIntervals.pop()
                noIntervals.append([left[0], right[1]])
            else:
                continue
                
        return noIntervals