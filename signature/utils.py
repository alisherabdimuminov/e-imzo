import random
import string


def generate_key():
    key: str = ""
    letters = string.ascii_letters
    digits = string.digits
    punctuations = string.punctuation
    for i in range(144):
        key += random.choice([random.choice(letters), random.choice(digits), random.choice(punctuations)])
    return key

def generate_filename():
    key: str = ""
    letters = string.ascii_letters
    digits = string.digits
    for i in range(15):
        key += random.choice([random.choice(letters), random.choice(digits)])
    return key
