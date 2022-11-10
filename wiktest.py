import wikipedia

while True:
    user_input = input("Q: ")
    print(wikipedia.summary(user_input, sentences = 3, auto_suggest=False))