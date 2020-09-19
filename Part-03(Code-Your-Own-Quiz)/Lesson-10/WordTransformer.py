def word_transformer(word):
    if word == "NOUM":
        return random_noun
    if word == "VERB":
        return random_verb
    else:
        return word[0]
