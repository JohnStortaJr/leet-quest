# LeetCode Problem 0127
# https://leetcode.com/problems/valid-palindrome

# Python experience: 2 weeks
# Time to solve: 1:00
# O(n)

# Ignore non-alphanumeric characters

class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        # Convert the string to a list and create a pointer to each end of the list
        stringList = list(s)
        frontIndex = 0
        backIndex = len(stringList)-1
        isPalindrome = True

        # Continue until both pointers arrive at the same element in the middle
        while frontIndex < backIndex:
            # If element is non-alphanumeric, move to the next element and continue
            if not stringList[frontIndex].isalnum():
                frontIndex += 1
            elif not stringList[backIndex].isalnum():
                backIndex -= 1
            elif stringList[frontIndex].lower() != stringList[backIndex].lower():
                # If the values do not match, then this is not a palindrome
                isPalindrome = False
                break
            else:
                # Still a potential palindrome, so move to the next elements and continue
                frontIndex += 1
                backIndex -= 1

        # If the loop completed, then the string is a palindrome
        return isPalindrome

mySolution = Solution()

print(mySolution.isPalindrome("A man, a plan, a canal: Panama"))
print("----")
print(mySolution.isPalindrome("race a car"))
print("----")
print(mySolution.isPalindrome("Was it a car or a cat I saw?"))
print("----")
print(mySolution.isPalindrome("tab a cat"))
print("----")
print(mySolution.isPalindrome(" "))
print("----")
print(mySolution.isPalindrome("  "))
print("----")
print(mySolution.isPalindrome(".,"))
