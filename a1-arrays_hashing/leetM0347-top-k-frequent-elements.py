# LeetCode Problem 0347
# https://leetcode.com/problems/top-k-frequent-elements

# Python Experience: 1 week
# Time to Solve: 1:00
# O(log n)

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Create a dictionary to store the count of each unique element from the list
        elementFrequency = {}

        for x in nums:
            if x in elementFrequency:
                # Number is already in the dictionary so increment the counter
                elementCounter = elementFrequency.get(x) + 1
                elementFrequency.update({x:elementCounter})
            else:
                # Number is not in the dictionary so add it with a count of 1
                elementFrequency.update({x:1})

        #print(f"Element count: {elementFrequency}")

        # Create a list contaning [count, key] from the dictionary
        sortedList = []
        for x in elementFrequency:
            sortedList.append([elementFrequency[x], x])
        #print(f"Count List: {sortedList}")
        
        # Reverse sort the list (by the first element) and slice the first k elements
        sortedList.sort(reverse=True)
        sortedList = sortedList[:k]
        #print(f"Sorted List: {sortedList}")

        # Create a new list with just the values from the sortedList
        finalList = []
        for x in sortedList:
            #print(x[1])
            finalList.append(x[1])
        

        return finalList




    
leet0347 = Solution()

print(leet0347.topKFrequent([1,1,1,2,2,3], 2))
print("----")
print(leet0347.topKFrequent([1], 1))
print("----")
print(leet0347.topKFrequent([-1,-1], 1))
