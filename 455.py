class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 数组为空的时候
        if len(g)==0 or len(s)==0:
            return 0

        # 排序
        g.sort()
        s.sort()

        # 比较
        i = j = 0
        count = 0
        while True:
            if g[i] <= s[j]:
                count += 1
                # 注意要len-1才是真实下标
                if i == len(g) - 1:
                    break
                elif j == len(s) - 1:
                    break
                else:
                    i += 1
                    j += 1
            else:
                if j == len(s) - 1:
                    break
                else:
                    j += 1
        return count


if __name__ == '__main__':
    su = Solution()
    result=su.findContentChildren([1,2],[1])
    print(result)
