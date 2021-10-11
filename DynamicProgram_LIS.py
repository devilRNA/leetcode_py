"""Problem Source:
https://www.luogu.com.cn/blog/pks-LOVING/junior-dynamic-programming-dong-tai-gui-hua-chu-bu-ge-zhong-zi-xu-lie

"""


def findLIS_length(arr):
    # initial
    dp = [1] * (len(arr))

    # solve
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)


if __name__ == '__main__':
    arr = [1, 7, 6, 2, 3, 4, 9]
    print(arr)
    print(findLIS_length(arr))
