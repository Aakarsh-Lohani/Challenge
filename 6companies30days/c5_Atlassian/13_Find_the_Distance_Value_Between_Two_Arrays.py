#https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
"""
1385. Find the Distance Value Between Two Arrays
Easy
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1
 

Constraints:

1 <= arr1.length, arr2.length <= 500
-1000 <= arr1[i], arr2[j] <= 1000
0 <= d <= 100
"""
"""#CORRECT 86ms
from typing import List
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c=0
        for i in arr1:
            test=1
            for j in arr2:
                val=abs(i-j)
                if val<=d:
                    test=0
                    break
            if test==1:
                c+=1
        return c

if __name__=="__main__":
    Solution=Solution()
    print(Solution.findTheDistanceValue([4,5,8],[10,9,1,8],2))
    print(Solution.findTheDistanceValue([1,4,2,3],[-4,-3,6,10,20,30],3))
    print(Solution.findTheDistanceValue([2,1,100,3],[-5,-2,10,-3,7],6))
"""
""" #CORRECT 76ms
from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance_value = 0
        for i in arr1:
            if all(abs(i - j) > d for j in arr2):
                distance_value += 1
        return distance_value
""" #CORRECT 60ms Binary search
from typing import List
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        distance_value = 0
        for i in arr1:
            pos = bisect.bisect_left(arr2, i)
            if pos == len(arr2):
                if abs(arr2[pos - 1] - i) > d:
                    distance_value += 1
            elif pos == 0:
                if abs(arr2[pos] - i) > d:
                    distance_value += 1
            else:
                if abs(arr2[pos] - i) > d and abs(arr2[pos - 1] - i) > d:
                    distance_value += 1
        return distance_value