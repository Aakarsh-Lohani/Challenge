#https://www.geeksforgeeks.org/problems/number-following-a-pattern3126/1
"""
Number following a pattern
Medium
Given a pattern containing only I's and D's. I for increasing and D for decreasing. Devise an algorithm to print the minimum number following that pattern. Digits from 1-9 and digits can't repeat.

Example 1:

Input:
D
Output:
21
Explanation:
D is meant for decreasing, so we choose the minimum number among all possible numbers like 21,31,54,87,etc.
Example 2:

Input:
IIDDD
Output:
126543
Explanation:
Above example is self- explanatory,
1 < 2 < 6 > 5 > 4 > 3
  I - I - D - D - D
Your Task:

You don't need to read input or print anything. Your task is to complete the function printMinNumberForPattern() which takes the string S and returns a string containing the minimum number following the valid number.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ Length of String ≤ 8



"""

class Solution:
    def printMinNumberForPattern(ob, S):
        # Initialize the stack and the result string
        stack = []
        result = ""

        # Initialize the current number
        num = 1

        # Process each character in the pattern
        for char in S:
            if char == 'I':
                # Push the current number to the stack, increment the number,
                # and pop all elements from the stack to the result
                stack.append(num)
                num += 1
                while stack:
                    result += str(stack.pop())
            else:  # char == 'D'
                # Push the current number to the stack and increment the number
                stack.append(num)
                num += 1

        # After processing all characters of the input pattern,
        # push the current number to the stack
        stack.append(num)

        # Pop all numbers from the stack to the result
        while stack:
            result += str(stack.pop())

        return result
    