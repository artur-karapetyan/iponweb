# You are given a 0-indexed string array words, where words[i] consists of lowercase English
# letters. In one operation, select any index i such that 0 &lt; i &lt; words.length and words[i - 1]
# and words[i] are anagrams, and delete words[i] from words. Keep performing this operation
# as long as you can select an index that satisfies the conditions.
# Return words after performing all operations. It can be shown that selecting the indices for
# each operation in any arbitrary order will lead to the same result.


def anagram(words):
    i = 1
    while i < len(words):
        if sorted(words[i - 1]) == sorted(words[i]):
            words.pop(i)
            i -= 1
        i += 1
    return words


words = ['abba', 'baba', 'bbaa', 'cd', 'cd']
print(anagram(words))
