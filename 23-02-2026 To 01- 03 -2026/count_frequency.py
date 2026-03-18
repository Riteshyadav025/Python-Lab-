def sort_by_frequency(s):
    from collections import Counter
    
    freq = Counter(s)
    
    sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
    
    result = ""
    for char, count in sorted_chars:
        result += char * count
    
    return result


# Given Input
s = "geeksforgeeks"
print(sort_by_frequency(s))
