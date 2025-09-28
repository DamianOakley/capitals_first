#Capitals first!
#https://www.codewars.com/kata/55c353487fe3cc80660001d4

def capitals_first(sentence: str):
    words = sentence.split()
    uppercase_words = []
    lowercase_words = []

    for word in words:
        if not word[0].isalpha():
            continue
        if word[0].isupper():
            uppercase_words.append(word)
        else:
            lowercase_words.append(word)

    product = " ".join(uppercase_words + lowercase_words)
    return product

print(capitals_first("Would you like some Mcdonalds?"))
print(capitals_first("1 Fish, 2 Fish"))
print(capitals_first("Can I please get 1 Baconator, please?"))

#This function breaks each sentence into a list of words, and then checks each word one by one.
#These words are sorted by uppercase and lowercase, with words that don't start with letters being skipped.
#The end result is then joined back into a single string.
