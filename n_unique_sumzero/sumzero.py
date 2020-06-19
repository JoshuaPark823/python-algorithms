"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
    Input: n = 5
    Output: [-7,-1,1,3,4]
    
    Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
    Input: n = 3
    Output: [-1,0,1]

Example 3:
    Input: n = 1
    Output: [0]

Constraints: 
    1 <= n <= 1000
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n == 1:
            return [0]
        
        # Closed List of unrepeatabe values
        closed_list = []
        
        # Case: n is even
        if n % 2 == 0:
            for i in range(1, int(n/2) + 1):
                closed_list.append(i)
                closed_list.append(i * -1)
        
        # Case: n is odd
        if n % 2 != 0:
            for i in range(1, int(n/2) + 1):
                closed_list.append(i)
                closed_list.append(i * -1)
            
            closed_list.append(0)
        
        return closed_list