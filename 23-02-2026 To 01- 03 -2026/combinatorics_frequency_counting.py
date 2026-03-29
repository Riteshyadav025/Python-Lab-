from math import factorial

def count_unique_vowel_strings(s):
    vowels = "aeiou"
 
    freq = {}
    for ch in s:
        if ch in vowels:
            freq[ch] = freq.get(ch, 0) + 1
    
    if not freq:
        return 0
    
    selection_ways = 1
    for count in freq.values():
        selection_ways *= count
    
    k = len(freq)
    permutation_ways = factorial(k)
    
    return selection_ways * permutation_ways


s = input().strip()
print(count_unique_vowel_strings(s))
