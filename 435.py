class Solution(object):

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 数组为0/1的情况
        length = len(intervals)
        if length == 0:
            return 0
        elif length == 1:
            return 0
        # 排序
        intervals.sort()
        # if len(intervals) == 0: return 0
        # intervals.sort(key=lambda x: x[1])
        print(intervals)

        # 比较
        pre = 0
        count = 0
        for i in range(1, length):
            if intervals[pre][1] > intervals[i][0]:
                print("killed"+str(intervals[i]))
                count += 1
            else:
                pre=i
                print("changed to "+str(intervals[pre]))

        return count

    def eraseOverlapIntervals2(self, intervals):
        if len(intervals) == 0: return 0
        intervals.sort(key=lambda x: x[1])
        count = 1 # 记录非交叉区间的个数
        end = intervals[0][1] # 记录区间分割点
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                count += 1
                end = intervals[i][1]
        return len(intervals) - count

if __name__ == '__main__':
    intervals=[[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
    su = Solution()
    result = su.eraseOverlapIntervals(intervals)
    print(result)

    result2=su.eraseOverlapIntervals2(intervals)
    print(result2)
