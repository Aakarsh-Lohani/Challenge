#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        # phone number to letter mappings
        mappings = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack
            
            # Get the letters that the current digit maps to, and loop through them
            for letter in mappings[digits[index]]:
                path.append(letter)  # Add the letter to our current path
                backtrack(index + 1, path)  # Move on to the next digit
                path.pop()  # Backtrack by removing the letter from our current path
            
        combinations = []
        backtrack(0, [])
        return combinations
if __name__=="__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))
    print(solution.letterCombinations(""))
    print(solution.letterCombinations("2"))
