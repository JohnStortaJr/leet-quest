# LeetCode Problem 0049
# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sortedList = []
        groupedList = []
        anagramSets = set()

        # sort each string and add to a new list and a set which stores each unique anagram string
        for x in range(len(strs)):
            anagramSets.add("".join(sorted(strs[x])))
            sortedList.append("".join(sorted(strs[x])))

        print(strs)
        #print(sortedList)
        #print(anagramSets)

        # Loop through each anagram string and add any matching list elements to the grouped list
        setCounter = 0
        for x in sorted(anagramSets):
            groupedList.append([])
            for y in range(0,len(sortedList)):
                if x == sortedList[y]:
                    groupedList[setCounter].append(strs[y])

            setCounter += 1

        return groupedList


    
leet0049 = Solution()

print(leet0049.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(leet0049.groupAnagrams([""]))    
print(leet0049.groupAnagrams(["a"]))    