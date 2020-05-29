# Count the number of prime numbers less than a non-negative number, n.

# Example:
#     Input: 10
#     Output: 4
#     Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0
    
        hash_map = {}
        num_primes = 0

        for i in range (n):
            hash_map[i] = True
        
        p = 2
        
        while (p * p <= n):
            if (hash_map[p] is True):
                for i in range (p * 2, n, p):
                    hash_map[i] = False

            p += 1

        hash_map[0] = False
        hash_map[1] = False

        for i in range (len(hash_map)):
            if hash_map[i] is True:
                num_primes += 1
        
        return num_primes

        


if __name__ == "__main__":

    test = Solution()
    print(test.countPrimes(100000))

    # temp = {2:True, 3:True, 5:True, 7:True}
    # print(len(temp.keys()))