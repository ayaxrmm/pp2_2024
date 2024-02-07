def reverse(sentence):
    words=sentence.split()
    reversed_words= reversed(words)
    reversed_sent = ""
    for word in reversed_words:
        reversed_sent += word + " "
    return reversed_sent
sentence = input("enter a sentence: ")
reverse = reverse(sentence)
print("reversed sentence: ", reverse)

