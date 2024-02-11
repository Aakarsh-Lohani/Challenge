#https://leetcode.com/problems/construct-the-longest-new-string/description/
"""
2745. Construct the Longest New String
Medium

You are given three integers x, y, and z.

You have x strings equal to "AA", y strings equal to "BB", and z strings equal to "AB". You want to choose some (possibly all or none) of these strings and concatenate them in some order to form a new string. This new string must not contain "AAA" or "BBB" as a substring.

Return the maximum possible length of the new string.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: x = 2, y = 5, z = 1
Output: 12
Explanation: We can concactenate the strings "BB", "AA", "BB", "AA", "BB", and "AB" in that order. Then, our new string is "BBAABBAABBAB". 
That string has length 12, and we can show that it is impossible to construct a string of longer length.
Example 2:

Input: x = 3, y = 2, z = 2
Output: 14
Explanation: We can concactenate the strings "AB", "AB", "AA", "BB", "AA", "BB", and "AA" in that order. Then, our new string is "ABABAABBAABBAA". 
That string has length 14, and we can show that it is impossible to construct a string of longer length.
 

Constraints:

1 <= x, y, z <= 50
"""
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        arr = sorted([(x, "AA"), (y, "BB"), (z, "AB")])
        res = []
        while arr:
            if len(arr) == 1:
                res.append(arr[0][1] * min(2, arr[0][0]))
                break
            use = min(arr[-1][0], 2 if arr[-2][0] * 2 >= arr[-1][0] else arr[-1][0] - arr[-2][0])
            res.append(arr[-1][1] * use)
            arr[-1] = (arr[-1][0] - use, arr[-1][1])
            if arr[-1][0] == 0:
                arr.pop()
            arr.sort()

        return len("".join(res))