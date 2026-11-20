"""Hashing & frequency patterns
• Use dictionaries for counts, lookups and grouping; use sets for seen/not-seen checks.
• Practice Two Sum using a dictionary; first understand the brute-force version.
• Practice contains duplicate, valid anagram, first unique character / frequency count.
• Discuss average-case dictionary lookup as O(1), while remembering worst-case nuance.
Checkpoint: identify when a hash map can replace an inner loop.
"""

# Dictionary for frequency counting
s = "satyavati"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
    
print(freq)

# Set for tracking seen elements
number = [2,4,6,2,8,11,4,4]
seen = set()
for num in number:
    if num in seen:
        print("Duplicate:", num)
    else:
        seen.add(num)