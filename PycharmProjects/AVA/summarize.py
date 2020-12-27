import random
import string
import nltk



def LemmatizeWords(words):
    return [lemmatizer.lemmatize(word) for word in words]


remove_punctuation = dict((ord(punctuation), None) for punctuation in string.punctuation)


def RemovePunctuations(text):
    return LemmatizeWords(nltk.word_tokenize(text.lower().translate(remove_punctuation)))

def reply_greeting(text):
    for word in text.split():
        if word.lower() in greeting_input_texts:
            return random.choice(greeting_replie_texts)

