# LeetCode Problem 0217
# https://leetcode.com/problems/contains-duplicate

# This one was trickier than expected due to the size of the test lists
# My first attempt did a basic nested list traversal, which worked,
#   but timed out when the list size got too large
# My next attempt popped the current element from the list and
#   then traversed what was left. It also worked and was slightly faster,
#   but still timed out
# Next I popped numbers from the list and checked them against a
#   list of numbers that were already popped. If found, then return true,
#   otherwise add the number to the popped list and try again.
#   Once again, this worked, but timed out with the longer list.
#### It seems this problem struggles to be solved if you traverse the full
#### list even once
# In the end, I looked at the solutions that others had submitted and
#   determined that the right approach was to not compare items within
#   the list, but rather create a copy using a data structure that does
#   not allow duplicates (such as a set). Then compare the length of each
#   If the lengths do not match, then there was a duplicate
# My solution below is not entirely mine. It was found in the solutions at
#   LeetCode.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        if len(nums) != len(set(nums)):
            return True
        return False

mySolution = Solution()

#print(mySolution.containsDuplicate([1,2,3,1]))
#print(mySolution.containsDuplicate([1,2,3,4]))
print(mySolution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
