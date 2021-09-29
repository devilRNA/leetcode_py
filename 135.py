class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        # 数组为空时
        if length == 0:
            return 0
        elif length == 1:
            return 1

        # 判断2个的情况
        if length == 2:
            if ratings[1] != ratings[0]:
                return 3
            else:
                return 2

        # 初始化数组
        cookies = ratings[:]
        for i in range(length):
            cookies[i] = 1

        # 长度length>=3的情况
        # 从左向右遍历
        i = 1
        while True:
            if ratings[i] > ratings[i - 1]:
                cookies[i] = cookies[i-1]+1
            if i == length - 1:
                break
            i += 1

        print(cookies)

        # 从右向左遍历
        j = length - 2
        while True:
            if ratings[j] > ratings[j + 1] and cookies[j]<=cookies[j+1]:
                cookies[j] = cookies[j+1]+1
            if j == 0:
                break
            j -= 1

        print(cookies)
        return sum(cookies)

    def candy2(self, ratings) :
        candyVec = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candyVec[i] = candyVec[i - 1] + 1
        print(candyVec)
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candyVec[j] = max(candyVec[j], candyVec[j + 1] + 1)
        print(candyVec)
        return sum(candyVec)


if __name__ == '__main__':
    ratings=[1,2,87,87,87,2,1]
    su = Solution()
    result = su.candy(ratings)
    print(result)

    result=su.candy2(ratings)
    print(result)
