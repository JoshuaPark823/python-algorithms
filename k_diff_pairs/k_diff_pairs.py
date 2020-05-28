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

        hash_map = {}
        total_count = 0

        # Absolute difference can never be negative
        if k < 0:
            return 0

        # Case where k == 0, we're just going to be counting the duplicates
        if k == 0:

            for element in nums:

                # If the element doesn't exist in the hash_map already, put it in with a count of 1
                if element not in hash_map:
                    hash_map[element] = 1

                # Else, increment the count of the element by 1 (duplicate)
                else:
                    hash_map[element] += 1

            # Loop through the numerous counts in the hash_map. Count the number of duplicate values
            for count in hash_map.values():
                if count >= 2:
                    total_count += 1

            return total_count

        # Remove the duplicates!
        nums_filtered = list(set(nums))

        # Case: k > 0. Fill the hash map up with (num : count) pairs
        for e in nums_filtered:
            if e not in hash_map:
                hash_map[e] = True

        # Loop through the individual counts in the hash map
        for value in hash_map.keys():

            if (value - k) in hash_map and hash_map[value - k] is True:
                total_count += 1
                hash_map[value] = False

            if (value + k) in hash_map and hash_map[value + k] is True:
                total_count += 1
                hash_map[value] = False

        return total_count


if __name__ == "__main__":

    test = Solution()

    print(test.findPairs([3, 1, 4, 1, 5], 2))    # --> 2
    print(test.findPairs([1, 2, 3, 4, 5], 1))    # --> 4
    print(test.findPairs([1, 3, 1, 5, 4], 0))    # --> 1
    print(test.findPairs([1, 2, 3, 4, 5], 4))    # --> 1
