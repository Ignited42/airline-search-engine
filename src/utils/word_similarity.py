# Author: Steven
# Description:
#   Utility function to detect how similar a word is to another based on its spelling.

ALPHABET_SIZE = 26

def compare_words(word1, word2):
    """
    Compares two words: word1 and word2, and gives a similarity index.\n
    The algorithm is known as Damerau-Levenshtein distance algorithm.\n
    Code from:\n
    - https://www.geeksforgeeks.org/damerau-levenshtein-distance/ \n
    - https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
    """
    word1 = str(word1)
    word2 = str(word2)

    matrix = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

    for i in range(len(word1) + 1):
        matrix[i][0] = i
    for j in range(len(word2) + 1):
        matrix[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i-1] == word2[j-1]:
                cost = 0
            else:
                cost = 1
            
            matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost)
            
            if (i > 1) and (j > 1) and word1[i-1] == word2[j-2] and word1[i-2] == word2[j-1]:
                matrix[i][j] = min(matrix[i][j], matrix[i-2][j-2] + cost)

    return matrix[len(word1)][len(word2)]
