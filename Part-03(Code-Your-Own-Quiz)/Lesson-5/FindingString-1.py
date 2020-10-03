text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""
noun_position = text.find("NOUN")
verb_position = text.find("VERB")
print(noun_position)
print(verb_position)
