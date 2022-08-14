from typing import List


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    word_count = {}
    # 1. normalize the paragraph string (replace non alphanumeric with a space and convert to lowercase)
    norm_words = (
        "".join(char.lower() if char.isalnum() else " " for char in paragraph)
    ).split()
    banned_words = set(banned)
    # 2. store each non-banned words with their counts in a dictionary
    for word in norm_words:
        if word not in banned_words:
            word_count[word] = word_count.get(word, 0) + 1
    # print(word_count)
    # 3. return the word with the highest count
    current_max = 0
    for word in word_count:
        if word_count[word] > current_max:
            current_max = word_count[word]
            most_common = word
    return most_common


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(mostCommonWord(paragraph, banned))
