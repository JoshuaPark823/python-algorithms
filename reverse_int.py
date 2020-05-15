# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
#     Input: 123
#     Output: 321

# Example 2:
#     Input: -123
#     Output: -321

# Example 3:
#     Input: 120
#     Output: 21

# Note:
    # Assume we are dealing with an environment which could only store integers within the 
    # 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume 
    # that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:

        # Create a reference to the input variable to avoid any shenanigans
        num = x
        return_val = 0

        # Toggle a Boolean if the input is a negative value, then make sure it's positive
        is_negative = False

        if num == 0:
            return num

        if num < 0:
            is_negative = True
            num = abs(num)

        # Make sure that if the number is divisible by 10 (ends in a zero), we remove them :)
        if num % 10 == 0:
            while num % 10 == 0:
                num /= 10

        # Initialize a HashTable to take advantage of the O(1) average case look-up times
        reversed_digits = {}

        # Initialize the position variable so that we can taret the end digits of the input
        position = 10
        
        # Keep looping while the number is greater than 0. We're going to subtract the last digit repeatedly
        while num > 0:

            # Isolate the value and store it in our HashTable
            single_digit = (int)((num % position)/(position/10))
            reversed_digits[position/10] = single_digit

            # Remove the last digit from the number
            num -= single_digit*(position/10)

            # Multiply the position variable by 10 to shift over to the next digit
            position *= 10

        # Initialize the multiplier for when we place the digits into their reversed positions
        power = len(reversed_digits)-1

        # Loop through the keys of the HashTable and sum the digits so they're in the reversed positions
        for key in reversed_digits.keys():

            return_val += reversed_digits.get(key) * (10 ** power)
            power -= 1

        # If the input was initially negative, re-apply the sign
        if (is_negative):
            return_val *= -1

        # Overflow check: if the reversed value is outside the constraints, return 0
        if return_val < (-1 * 2**31) or return_val > (2 ** 31 - 1):
            return 0

        return return_val