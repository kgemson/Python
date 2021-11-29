def sentence_maker(phrase):
    capitalized = phrase.lower().capitalize()

    interrogatives = ("how","why","when","where","what")

    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "/end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))