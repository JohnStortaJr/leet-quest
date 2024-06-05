# LeetCode Problem 0238
# https://leetcode.com/problems/product-of-array-except-self

# Python experience: 1 week
# Time to Solve: :30
# O(n)

# The challenge of this problem is more about solving it to fit within the O(n) constraints
# rather than the problem itself
# This problem highlights one of my concerns with LeetCode. It is too focused on the Big O rather
# than the solution. The code here works and was accepted by NeetCode. But LeetCode rejects it
# because it times out for a very large set of inputs. The accepted solutions all seem to use
# the same logical approach as this code, but implement it differently (using prefix vs Math)
# I feel this discourages entry-level developers by implying that there is only a single
# method for solving the problem.
# This code is not the best code, but it solves the problem defined.
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
