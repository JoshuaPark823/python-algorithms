"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].
"""

from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        # Initialize the count as 0
        count = 0

        # We're gonna use a hashmap to take advantage of its lookup times, otherwise we'd have to do this
        # in like quadratic or O(nlogn) time which is too slow
        nums_filtered = list(set(nums))
        hash_map = {}

        # We know the max size is 10,000. Initialize a dictionary of the max size with (int : False) pairs.
        # Now our keys contain all values from 0 -> 10,000
        for i in range (10000):
            hash_map[i] = False
        
        # Go through the hash man again and overwrite all the booleans to True if they're a value in the array.
        # Should look something like:
        #   {(0:False), (1:True), (2:False), (3:True), (4:True), (5:True), (6:False), (7:False), (.....)}
        for element in nums_filtered:
            hash_map[element] = True
        
        # Absolute difference -> |a - b| = k
        #   Split into two cases: (a + b) = k
        #                        -(a + b) = k --> -a - b = k

        # We know for sure that A is contained in the hash map. We're also given K. 
        # This means we can check if K-A exists (is True), or K+A exists (is True)

        for i in range(len(nums) - 1):

            a = nums[i]

            # If hash_map at abs(k-a) is True, we increment the count
            if hash_map[abs(k - a)]:
                count += 1

            print(hash_map)

        print(count)
        return count


if __name__ == "__main__":

    test = Solution()

    # test.findPairs([3, 1, 4, 1, 5], 2)
    test.findPairs([1, 2, 3, 4, 5], 1)
    # test.findPairs([1, 3, 1, 5, 4], 0)
