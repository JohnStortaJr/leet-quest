# LeetCode Problem 0238
# https://leetcode.com/problems/product-of-array-except-self

# Python experience: 1 week
# Time to Solve: N/A
# O(n)

# The challenge of this problem is more about solving it to fit within the O(n) constraints
# rather than the problem itself

# This code was pulled from the existing LeetCode solutions
# This approach is similar to my approach in that it captures the products of elements
# before and after each index and then combines them.
# This solution runs through the list multiple times to perform the calculations
# My solution uses the math module to do this while traversing the list just once
# See leetM0238a-product-of-array-except-self.py for my solution using the math module
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        numberCount = len(nums)

        leadingProducts = [1] * numberCount
        trailingProducts = [1] * numberCount
        newList = [1] * numberCount

        #print(f"Input: {nums}")

        # Create a list containing the product of all numbers BEFORE the current element
        for i in range(1, numberCount):
            leadingProducts[i] = leadingProducts[i-1] * nums[i-1]
        #print(f"Prefix: {prefix}")
        
        # Create a list containing the product of all numbers AFTER the current element
        for i in range(numberCount-2, -1, -1):
            trailingProducts[i] = trailingProducts[i+1] * nums[i+1]
        #print(f"Suffix: {suffix}")
        
        # Create a list containing the product leading and trailing products at each index
        for i in range(numberCount):
            newList[i] = leadingProducts[i] * trailingProducts[i]
        
        return newList


leet0238 = Solution()

print(leet0238.productExceptSelf([1,2,3,4]))
print("----")
print(leet0238.productExceptSelf([-1,1,0,-3,3]))
print("----")
print(leet0238.productExceptSelf([0,0]))
