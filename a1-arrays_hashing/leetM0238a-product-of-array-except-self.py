# LeetCode Problem 0238
# https://leetcode.com/problems/product-of-array-except-self

# Python experience: 1 week
# Time to Solve: :30
# O(n)

# The challenge of this problem is more about solving it to fit within the O(n) constraints
# rather than the problem itself

# My approach is to capture the products of elements
# before and after each index and then combine them.
# My solution uses the math module to do this while traversing the list just once
# See leetM0238b-product-of-array-except-self.py for the solution using a different approach without the math module
import math

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Due to the O(n) limitation, the solution cannot contain any nested loops (one time through)
        # The instructions also indicate that division cannot be used
        #print(nums)

        newList = []

        # Each element is the product of nums[:x-1] * nums[x+1:]
        for x in range(0,len(nums)):
            #print(f"{nums[:x]} * {nums[x+1:]} = {math.prod(nums[:x])} * {math.prod(nums[x+1:])}")

            newList.append(math.prod(nums[:x]) * math.prod(nums[x+1:]))
                                  
        return newList



leet0238 = Solution()

print(leet0238.productExceptSelf([1,2,3,4]))
print("----")
print(leet0238.productExceptSelf([-1,1,0,-3,3]))
print("----")
print(leet0238.productExceptSelf([0,0]))
