class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = []
        index = 0

        # which word is longer
        # loop through shorter word
        word1List = []
        word2List = []

        for x in word1:
            word1List.append(x)

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
