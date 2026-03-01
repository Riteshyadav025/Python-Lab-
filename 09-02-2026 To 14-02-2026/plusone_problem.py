digits = [1, 2, 3]

def plusOne(digits):
    n = len(digits)
    
    # Start from the last digit
    for i in range(n - 1, -1, -1):
        
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    
    # If all digits were 9
    return [1] + digits

print("Result:", plusOne(digits))
