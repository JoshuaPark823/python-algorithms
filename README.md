# Collection of Algorithmic Solutions written in Python3

## Structure
- At the top of each file, the problem's prompt, example outputs, and constraints/restrictions will be posted as a comment.
- Following the constraints, solution is written below.
- Time complexity will be included in the commit message.

## Purpose
- To gain further proficiency with algos and data structures.
- To gain further proficiency with time & space complexity optimization.

## Notable Implementations
- reverse_int.py: </br>
</br>Faster than 60% of all other Python3 submissions. Achieved this by using a HashTable to store the individual digits as index:digit  pairs. By taking advantage of the HashTable's constant lookup time I managed to keep the runtime pretty low although space complexity took a small hit.

## Major Bugs
- count_primes.py: </br>
</br>Double Counting: The current implementation uses nested for loops to iterate through the array of primes and subtracts 1 from the `num_primes` if it comes across one where `array[numerator] % array[denominator] == 0`. However, this results in a miscount where if n is 143, it'll substract one for when numerator = 11 and also for numerator = 13. This issue has been fixed by setting a boolean marker. 
</br> Currently trying to optimize the time complexity but having trouble getting the algorithm below
O(n*log(n)) time.
