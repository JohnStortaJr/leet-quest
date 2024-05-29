# LeetCode problem 1768
# https://leetcode.com/problems/merge-strings-alternately
# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# Paste the contents of the mergeAlternately function into LeetCode

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = []

        word1List = []
        for x in word1:
            word1List.append(x)

        word2List = []
        for x in word2:
            word2List.append(x)

        for x in range(0, max(len(word1List),len(word2List))):
            if x < len(word1):
                mergedString.append(word1List[x])

            if x < len(word2):
                mergedString.append(word2List[x])
            
            print(mergedString)

        return ''.join(mergedString)


runmerge = Solution()

print(runmerge.mergeAlternately("first", "second"))
