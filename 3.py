
sentence = "We are not makers of history. We are made by history."


words = sentence.split()


words_with_o = [word for word in words if 'o' in word]

print("Words containing at least one letter ‘o’:", words_with_o)
