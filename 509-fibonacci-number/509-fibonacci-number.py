class Solution:
    def fib(self, n: int) -> int:
        num_2, num_1 = 0, 1

        for i in range(n):
            num_2, num_1 = num_1, num_1 + num_2
            
        return num_2
    
            
        