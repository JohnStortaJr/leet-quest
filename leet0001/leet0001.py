# LeetCode Problem 0001

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        solution = []

        # Iterate through each number pair in the list
        for x in range(0,len(nums)-1):
            for y in range(x+1, len(nums)):
                # If the sum of the two values equals the target, then make note of the indexes and exit
                if nums[x]+nums[y] == target:
                    solution.append(x)
                    solution.append(y)
                    break

        return solution
    
leet0001 = Solution()

print(leet0001.twoSum([2,7,11,15], 9))    