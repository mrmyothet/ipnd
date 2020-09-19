sentence = "A Noun went on a walk. It can Verb really fast."
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

Noun_replacement = "dog"
Verb_replacement = "run"
new_sentence = substring1 + Noun_replacement + substring2 + Verb_replacement + substring3
print (new_sentence)
