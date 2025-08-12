"here we will build the password generator whcih will take the arguements like the length of the password , number of special characters, uppercase letters, lowercase letters and the digits"

import string
import random
import secrets


def generate_password(l,u,p,d, total):
    lwr = random.choices(string.ascii_lowercase, k = l)
    uppr = random.choices(string.ascii_uppercase, k = u)
    punctuations = random.choices(string.punctuation, k = p)
    digits = random.choices(string.digits, k = d)
    alphabet = lwr + uppr + punctuations + digits
    
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(total))
        ispunct = total - (sum(c.isupper() for c in password) + sum(c.islower() for c in password) + sum(c.isdigit() for c in password))
        if (sum(c.islower() for c in password) == l
                and sum(c.isupper() for c in password) == u
                and sum(c.isdigit() for c in password) == d
                and (ispunct == p)) :
            break
    return password

def random_passphrase_generator(word_count):
    with open('word_list.txt') as f:
        #words list is taken from here https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases
        words = [word.strip() for word in f]
        passphrase = ' '.join(secrets.choice(words) for i in range(word_count))
    return passphrase

