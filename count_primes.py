# Count the number of prime numbers less than a non-negative number, n.

# Example:
#     Input: 10
#     Output: 4
#     Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution:
    def countPrimes(self, n: int) -> int:

        # Some edge case checks. The modifications to the loop only modify it by a constant so the change to the 
        # complexity of the first loop on line 28 is still O(n). But conditionals also run in constant time so w/e.
        if n <= 2:
            return 0

        elif n <= 5:
            if n == 3:
                return 1
            return 2

        elif n <= 7:
            return 3

        # Initialize array_primes with a few early prime numbers.
        array_primes = [2,3,5,7]

        # For all the odd integers from 1 -> n, if they don't divide 3, 4, 5, and 7, add them into the array.
        for number in range(11, n, 2):
            
            if number % 3 == 0 or number % 4 == 0 or number % 5 == 0 or number % 7 == 0:
                continue

            array_primes.append(number)

        num_primes = len(array_primes)

        # Loop through the array of perceived primes and filter all non-prime numbers out
        for d_index in range(len(array_primes)):
            for n_index in range(d_index + 1, len(array_primes)):

                # To avoid double-counting of a large number with both factors in the same set, set it as
                # negative after counting for it, then add a sign check in the conditional.
                if array_primes[n_index] > 0 and array_primes[n_index] % array_primes[d_index] == 0:
                    num_primes -= 1
                    array_primes[n_index] = -array_primes[n_index]

        return num_primes


if __name__ == "__main__":

    test = Solution()
    print(test.countPrimes(100000))

    # temp = {2:True, 3:True, 5:True, 7:True}
    # print(len(temp.keys()))