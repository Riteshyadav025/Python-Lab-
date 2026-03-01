strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
    anagram_dict = {}
    
    for word in strs:
        # Sort the word to create a key
        key = "".join(sorted(word))
        
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]
    
    return list(anagram_dict.values())

print(groupAnagrams(strs))
