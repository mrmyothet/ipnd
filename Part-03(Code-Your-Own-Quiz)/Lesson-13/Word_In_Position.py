def word_in_pos(word,parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]
print(word_in_pos(test_cases[0], parts_of_speech))
print(word_in_pos(test_cases[1], parts_of_speech))
print(word_in_pos(test_cases[2], parts_of_speech))
print(word_in_pos(test_cases[3], parts_of_speech))
