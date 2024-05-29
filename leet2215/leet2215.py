# LeetCode Problem 2215 -- IN PROGRESS
# https://leetcode.com/problems/find-the-difference-of-two-arrays
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # Some additional information about the above argument notation
        # nums1: List[int] indicates that the passed value will be named nums1 within this function
        # : List[int] is a tag that specifies more specifically what type this argument will be
        # -> List[List[int]] is a tag that indicates what will be returned from this function
        # In this case it returns a List of Lists.

        answer = []
        answer1 = []
        answer2 = []

        for x in nums1:
            if x not in nums2:
                if x not in answer1:
                    answer1.append(x)
        
        for x in nums2:
            if x not in nums1:
                if x not in answer2:
                    answer2.append(x)

        answer.append(answer1)
        answer.append(answer2)

        return answer
    

listDifference = Solution()

print(listDifference.findDifference([1,2,3], [2,4,6]))
#print(listDifference.findDifference([1,2,3,3], [1,1,2,2]))