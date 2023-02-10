# NOT YET FINISHED


# A transformation sequence from word beginWord to word endWord using a list wordList is a
# sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# ● Every adjacent pair of words differs by a single letter.
# ● Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in
# wordList.
# ● sk == endWord
# Given two words, beginWord and endWord, and a list wordList, return all the shortest
# transformation sequences from beginWord to endWord, or an empty list if no such sequence
# exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
# Example 1:
# Input: beginWord = 'hit', endWord = 'cog', wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
#
# Output: [['hit','hot','dot','dog','cog'],['hit','hot','lot','log','cog']

def transformation(beginWord, endWord, wordList):
    wordList = set(wordList)
    if endWord not in wordList:
        return []

    n = len(beginWord)
    dict = {}
    for word in wordList:
        for i in range(n):
            temp = word[:i] + "*" + word[i + 1:]
            if temp not in dict:
                dict[temp] = []
            dict[temp].append(word)

    current = [beginWord]
    visited = {beginWord: 0}
    answer = []
    while current:
        next = []
        level = visited[current[0]] + 1
        for word in current:
            if word == endWord:
                answer.append([beginWord] + [w for w in current if w != beginWord])
                for i in range(n):
                    s = word[:i] + "*" + word[i + 1:]
                    for nextWord in dict.get(s, []):
                        if nextWord not in visited:
                            next.append(nextWord)
                            visited[nextWord] = level
                current = next
    return answer


beginWord = 'hit'
endWord = 'cog'
wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
print(transformation(beginWord, endWord, wordList))
