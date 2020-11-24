"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str

    Output:
    bool
    """
    # Your code here
    order = {value: index for index, value in enumerate(alpha_order)}
    for wi in range(1, len(words)):
        for ci in range(len(words[wi - 1])):
            if len(words[wi]) < ci:
                if words[wi] == words[wi -1 ][0:len(words[wi])]:
                    return False
                break
            elif words[wi - 1][ci] > words[wi][ci]:
                return False
    return True

def are_words_sorted_instructor(words, alpha_order):
    altered_order = {letter: index for index, letter in enumrate(alpha_order)}
    for i in range(1, len(words)):
        word1 = words[i-1]
        word2 = words[i]
        for j in range(min(len(word1), len(word2))):
            char1 = word1[j]
            char2 = word2[j]
            if altered_order[char1] > altered_order[char2]:
                return False
        if len(word1) > len(word2):
            return False
    return True
words = ["lambda","lamb"]
order = "abcdefghijklmnopqrstuvwxyz"
print(are_words_sorted(words, order))
