# LeetCode Problem 0128
# https://leetcode.com/problems/longest-consecutive-sequence

# Python experience: 1 week
# Time to Solve: 1:00
# O(n log n)
# I use a sort which makes this a log n and then the iteration adds an n

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # Sort the list
        nums.sort()
        print(nums)
        sortedList = [nums[0]]

        # Create a set from the list to remove duplicates
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                sortedList.append(nums[i])

        #print(sortedList)

        # Initialize counter to 0
        currentSequence = 1
        maxSequence = 1

        # iterate through the list
        for i in range(0,len(sortedList)-1):
            # Is the next value in the list one greater than the current value
            #print(f"{sortedList[i+1]} - {currentSequence} - {maxSequence}")
            if sortedList[i+1] == sortedList[i]+1:
                currentSequence += 1
            else:
                # Is this sequence longer than the longest found so far
                #print(f">>{currentSequence} - {maxSequence}<<")
                if currentSequence > maxSequence:
                    maxSequence = currentSequence
                
                currentSequence = 1

        if currentSequence > maxSequence:
            maxSequence = currentSequence

        return maxSequence
 

leet0128 = Solution()

print(leet0128.longestConsecutive([100,4,200,1,3,2]))
print("----")
print(leet0128.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print("----")
print(leet0128.longestConsecutive([0,3,2,5,4,6,1,1]))
print("----")
print(leet0128.longestConsecutive([2,20,4,10,3,4,5]))
print("----")
print(leet0128.longestConsecutive([]))
