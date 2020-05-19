# Count the number of prime numbers less than a non-negative number, n.

# Example:
#     Input: 10
#     Output: 4
#     Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution:
    def countPrimes(self, n: int) -> int:

        # Plan: We will be implementing the Algorithm for Sieve of Eratosthenes
        # Initialize an array of odd numbers from 2->N (have 2 initially inside the array)
        # Do a little cleaning while initializing so that numbers divisible by 3,4,5, and 7 aren't added.
        array_odd = [2]

        # For all the odd integers from 1 -> n, if they don't divide 3, 4, 5, and 7, add them into the array.
        for number in range(3, n, 2):
            
            if number % 3 == 0 or number % 4 == 0 or number % 5 == 0 or number % 7 == 0:
                continue

            array_odd.append(number)

        # Call ur Sieve function with the filtered array of numbers and index = 0
        return len(self.sieve(array_odd, 1))

    def sieve(self, array, index: int):

        if index > len(array):
            return array

        else:
            for num in range(index, len(array)-1):
                if array[num] % array[index] == 0:
                    print(array[num])
                    print(array[index])
                    array.pop(num)

            print(array)
            return self.sieve(array, index+1)

if __name__ == "__main__":

    test = Solution()
    test.countPrimes(100)