class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer limits
        MAX_INT = 2147483647        # 2^31 - 1
        MIN_INT = -2147483648       # -2^31
        
        # Handle the specific overflow edge case: -2^31 / -1
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine the sign of the result
        # XOR of sign bits: if exactly one is negative, the result is negative
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values to simplify logic
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        
        # Main bit manipulation logic:
        # Subtract the largest multiple (divisor * 2^k) that fits into dividend
        while dvd >= dvs:
            temp_divisor = dvs
            multiple = 1
            # Double the divisor multiple until it's larger than the remaining dividend
            # temp_divisor << 1 is equivalent to temp_divisor * 2
            while dvd >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the found multiple from the dividend and add to quotient
            dvd -= temp_divisor
            quotient += multiple
            
        # Apply the sign and return the result clamped to 32-bit limits
        return -quotient if is_negative else quotient
