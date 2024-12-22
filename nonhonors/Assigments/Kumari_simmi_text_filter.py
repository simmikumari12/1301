def text_filter(user_input):
    banned_words = ["Turkey", "Dog","Fox","Cat","Chicken"]
    words = user_input.split()
    [words.remove(word) for word in words if word in banned_words]
    print(words)

text_filter(str(input("Input message: ")))
