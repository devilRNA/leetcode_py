from numpy import zeros


def get_LCS_arr(X, Y):
    """根据算法导论构造的函数，要特别注意数组边界的问题
    主要有两点：
    1.range（）函数是左闭右开的，若要包括边界，需要+1
    2.由字符串转数组的时候，由于循环体是从i=1,j=1开始的，这意味着我们访问字符串数组应该是【i-1】、【j-1】
    """
    m = len(X) + 1
    n = len(Y) + 1
    c = [[0 for i in range(n)] for i in range(m)]
    b = [[0 for i in range(n)] for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "*"

            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "UP"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "L"
    return c, b


def printLCS(arr, string, i, j):
    if i == 0 or j == 0:
        return
    if arr[i][j] == '*':
        printLCS(arr, string, i - 1, j - 1)
        print(string[i - 1].strip())
    elif b[i][j] == "UP":
        printLCS(arr, string, i - 1, j)
    else:
        printLCS(arr, string, i, j - 1)





def val_list(s1, s2):
    """参考了一下别人求LCS的辅助函数，Source: https://www.cnblogs.com/7749ha/p/9160868.html"""
    # 两个字符串的长度
    len_s1 = len(s1) + 1
    len_s2 = len(s2) + 1
    # 方向列表
    direction_list = []
    # 生成len_s2+1行len_s1+1列的全0列表
    res = zeros((len_s2, len_s1))
    direction = zeros((len_s2, len_s1))
    # print(res_list)
    for i in range(0, len_s2 - 1):
        for j in range(0, len_s1 - 1):
            # 判断是否相等
            if s1[j] == s2[i]:
                res[i + 1, j + 1] = res[i, j] + 1
                # 1左上 2 上 3左
                direction[i + 1, j + 1] = 1
            else:
                if res[i + 1, j] > res[i, j + 1]:
                    res[i + 1, j + 1] = res[i + 1, j]
                    direction[i + 1, j + 1] = 3
                else:
                    res[i + 1, j + 1] = res[i, j + 1]
                    direction[i + 1, j + 1] = 2
    return res, direction


if __name__ == '__main__':
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    ss1 = [str(i) for i in s1]
    ss2 = [str(i) for i in s2]

    c, b = get_LCS_arr(ss1, ss2)
    printLCS(b, ss1, len(ss1), len(ss2))

    # for i in range(len(c)):
    #     print(c[i])
    # for i in range(len(b)):
    #     print(b[i])
