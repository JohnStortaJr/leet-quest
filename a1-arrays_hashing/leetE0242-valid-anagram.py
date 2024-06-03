# LeetCode Problem 0242
# https://leetcode.com/problems/valid-anagram

# Not the fastest solution, but I feel that the goal is to first solve the problems
# logically. Many of the other solutions just used the sorted() function. This is fine
# and in the real world would be better, but I believe the test is it to first come 
# up with the logic on my own and then use shortcuts to improve performance.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        result = True

        # If the lengths do not match, then it cannot be an anagram
        if len(s) != len(t):
            return False

        # Check each letter in s
        for x in range(len(s)):
            # If it is in t, then increment the counter and remove from t so it is not found again
            if t.find(s[x]) >= 0:
                t = t.replace(s[x],"",1)
            else:
                result = False
                break

            # print(f"s: {s} t: {t}")

        return result

mySolution = Solution()

print(mySolution.isAnagram("anagram", "nagaram"))
print(mySolution.isAnagram("rat", "car"))
print(mySolution.isAnagram("a", "ab"))
print(mySolution.isAnagram("cab", "ab"))
print(mySolution.isAnagram("aa", "a"))
print(mySolution.isAnagram("aacc", "ccac"))
