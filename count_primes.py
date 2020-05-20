# Count the number of prime numbers less than a non-negative number, n.

# Example:
#     Input: 10
#     Output: 4
#     Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution:
    def countPrimes(self, n: int) -> int:

        # Plan: We will be implementing the Algorithm for Sieve of Eratosthenes (With our variation)
        # Initialize an array of odd numbers from 2->N (have 2 initially inside the array)
        # Do a little cleaning while initializing so that numbers divisible by 3,4,5, and 7 aren't added.
        array_primes = [2,3,5,7]
        duplicates = {}

        # For all the odd integers from 1 -> n, if they don't divide 3, 4, 5, and 7, add them into the array.
        for number in range(11, n, 2):
            
            if number % 3 == 0 or number % 4 == 0 or number % 5 == 0 or number % 7 == 0:
                continue

            array_primes.append(number)

        num_primes = len(array_primes)
        print(num_primes)

        # Loop through the array of perceived primes and filter all non-prime numbers out
        for d_index in range(len(array_primes)):

            if d_index + 1 < len(array_primes):
                for n_index in range(d_index + 1, len(array_primes)):

                    # For each number that divides the number at the current index, decrease the number of primes by 1
                    if array_primes[n_index] % array_primes[d_index] == 0:
                        print("FOUND ONE")
                        print(array_primes[n_index])
                        print(array_primes[d_index])

                        # Remove it from the array
                        duplicates.append(array_primes.pop(n_index))
                        num_primes -= 1
                        print(num_primes)

            print(array_primes)

        print(num_primes)
        return num_primes


if __name__ == "__main__":

    test = Solution()
    test.countPrimes(200)

    