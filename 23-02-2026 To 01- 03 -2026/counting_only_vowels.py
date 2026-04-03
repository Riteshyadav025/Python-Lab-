def count_vowel_strings(arr):
    vowels = set('aeiou')
    count = 0
    
    for word in arr:
        if all(char in vowels for char in word):
            count += 1
            
    return count


# Example usage
arr = ["aeio", "aa", "bc", "ot", "cdbd"]
print(count_vowel_strings(arr)) 
