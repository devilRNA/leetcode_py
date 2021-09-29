from typing import List


class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if expression.isdigit():
            return [int(expression)]

        res = []
        for i,char in enumerate(expression):
            if char in ['+','-','*']:
                #divide & conquer:
                left = self.diffWaysToCompute(expression[:i])
                right  = self.diffWaysToCompute(expression[i+1:])

                # combine & calculate
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l+r)
                        if char == '-':
                            res.append(l - r)
                        if char == '*':
                            res.append(l * r)

        return res
