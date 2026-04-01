def count_even_letters(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1
    count = 0
    for value in freq.values():
        if value % 2 == 0:
            count += 1

    return count

# Example
s = "abacaba"
print(count_even_letters(s))
