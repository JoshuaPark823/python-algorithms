"""
Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution:
    def countPrimes(self, n: int) -> int:

        # If the input number is less than or equal to 2, there won't be any more primes.
        if n <= 2:
            return 0
    
        hash_map = {}
        num_primes = 0

        # Fill the hash map with (num : boolean) pairs, True indicating that it IS prime
        for i in range (n):
            hash_map[i] = True
        
        p = 2
        
        # While the square of the number is less than the input, n, loop
        while (p * p <= n):

            # Set the multiples of p so that they're now False (not prime)
            if (hash_map[p] is True):
                for i in range (p * 2, n, p):
                    hash_map[i] = False
            p += 1

        # Just setting 0 and 1 as False
        hash_map[0] = False
        hash_map[1] = False

        # Loop through the hash map and increment the counts
        for i in range (len(hash_map)):
            if hash_map[i] is True:
                num_primes += 1
        
        return num_primes

if __name__ == "__main__":

    test = Solution()
    print(test.countPrimes(100000))

