"""
Character Frequency

Description:
Counts the frequency of each character in a string using a dictionary.

Time Complexity: O(n)
Space Complexity: O(n)
"""
s=input("Enter a word: \n")
s=s.lower()
freq={}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("\nCharacter Frequency:")
for ch,count in freq.items():
    print(ch,":",count)
    
