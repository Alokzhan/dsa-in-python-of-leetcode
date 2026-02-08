class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        MAX_INT = 2147483647       
        MIN_INT = -2147483648       
        
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        
        is_negative = (dividend < 0) ^ (divisor < 0)
      
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        
       
        while dvd >= dvs:
            temp_divisor = dvs
            multiple = 1
            
            while dvd >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            
            dvd -= temp_divisor
            quotient += multiple
            
       
        return -quotient if is_negative else quotient
