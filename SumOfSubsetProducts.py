'''
Solution:
1. Apart from Backtracking solution which is exponential, there is a direct computation for caclulating the sum of product
    of subsets in an array.
2.  ===> [ (1 + a1)(1 + a2)(1 + a3)...(1 + an) - 1 ]

Time Complexity: O(n)
Space Complexity:   O(1)

--- Handled all edge cases and the rest is a direct formula, so the below function will work for all testcases.
'''


class SumOfSubsetProducts:

    def getSum(self, nums) -> int:

        #   edge case check
        if (nums == None or len(nums) == 0):
            return 0

        product = 1

        #   perform product update based on the above formula
        for num in nums:
            product = product * (1 + num)

        return (product - 1)

if __name__ == '__main__':

    ssp = SumOfSubsetProducts()
    nums = [1, 2, 3]
    print(ssp.getSum(nums))