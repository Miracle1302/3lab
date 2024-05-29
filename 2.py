
word1 = "programming"
word2 = "python"


set_word1 = set(word1)
set_word2 = set(word2)


common_letters = set_word1 & set_word2


unique_common_letters = [char for char in common_letters if word1.count(char) == 1 and word2.count(char) == 1]

print("Letters that appear in both words only once:", unique_common_letters)
