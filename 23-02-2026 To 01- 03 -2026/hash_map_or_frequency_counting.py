def shortest_vowel_substring(s1, s2):
    required = set(s1)  
    count = {}
    formed = 0
    left = 0
    min_len = float('inf')

    for right in range(len(s2)):
        char = s2[right]

        if char in required:
            count[char] = count.get(char, 0) + 1
            if count[char] == 1:
                formed += 1

        while formed == len(required):
            min_len = min(min_len, right - left + 1)

            left_char = s2[left]
            if left_char in required:
                count[left_char] -= 1
                if count[left_char] == 0:
                    formed -= 1

            left += 1

    return min_len if min_len != float('inf') else -1


s1 = "ae"
s2 = "acbaudeq"
print(shortest_vowel_substring(s1, s2))
