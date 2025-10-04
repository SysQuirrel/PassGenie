import string
import random
import secrets
import shutil
import os
def main():

    msg_1 = r""" 
         ___                      ___                           
        (  _`\                   (  _`\                _        
        | |_) )  _ _   ___   ___ | ( (_)   __    ___  (_)   __  
        | ,__/'/'_` )/',__)/',__)| |___  /'__`\/' _ `\| | /'__`\
        | |   ( (_| |\__, \\__, \| (_, )(  ___/| ( ) || |(  ___/
        (_)   `\__,_)(____/(____/(____/'`\____)(_) (_)(_)`\____)"""

    msg_2 = r"""
    <!-- .-------------------------------------------------------. -->
    <!-- |               !!!!!!!Instructions!!!!!!!              | -->
    <!-- | You can generate passwords and passphrases using this | -->
    <!-- | program.                                              | -->
    <!-- | You can specify the number of lowercase and uppercase | -->
    <!-- | letters, numbers, and special symbols.                | -->
    <!-- | It is recommended to generate at least 14 characters  | -->
    <!-- | long password.                                        | -->
    <!-- | Use all the elements to strengthen your password.     | -->
    <!-- | For passphrases generate at least 4 words.            | -->
    <!-- | To copy the generated password or passphrase, select  | -->
    <!-- | what you need to copy and press Shift+Ctl+C.          | -->
    <!-- | If you enter large numbers as input then the program  | -->
    <!-- | may take few seconds to few minutes generate the      | -->
    <!-- | long password. Don't press any keys during that time. | -->
    <!-- '-------------------------------------------------------' -->"""

    msg_3 = r"""
         ____   __   ____  ____  _  _   __  ____  ____     
        (  _ \ / _\ / ___)/ ___)/ )( \ /  \(  _ \(    \    
         ) __//    \\___ \\___ \\ /\ /(  O ))   / ) D (    
        (__)  \_/\_/(____/(____/(_/\_) \__/(__\_)(____/    
         ___  ____  __ _  ____  ____   __  ____  __  ____ 
        / __)(  __)(  ( \(  __)(  _ \ / _\(_  _)/  \(  _ \
       ( (_ \ ) _) /    / ) _)  )   //    \ )( (  O ))   /
        \___/(____)\_)__)(____)(__\_)\_/\_/(__) \__/(__\_)"""

    msg_4 = r"""
         ___  __   ___  ___  ___  _  _  ___    __   ___  ___ 
        (  ,\(  ) / __)/ __)(  ,\( )( )(  ,)  (  ) / __)(  _)
         ) _//__\ \__ \\__ \ ) _/ )__(  )  \  /__\ \__ \ ) _)
        (_) (_)(_)(___/(___/(_)  (_)(_)(_)\_)(_)(_)(___/(___)
          __  ___  _  _  ___  ___    __  ____  __  ___       
         / _)(  _)( \( )(  _)(  ,)  (  )(_  _)/  \(  ,)      
        ( (/\ ) _) )  (  ) _) )  \  /__\  )( ( () ))  \      
         \__/(___)(_)\_)(___)(_)\_)(_)(_)(__) \__/(_)\_)"""

    msg_5 = r"""Whoa!! very long  password.Don't press any keys warrior."""

    columns = shutil.get_terminal_size().columns
    padded_msg_1 = msg_1.center(columns)
    print(f"\033[36m{padded_msg_1}\033[0m")
    print()
    padded_msg_2 = msg_2.center(columns)
    print(f"\033[31m{padded_msg_2}\033[0m")
    print()
    while True:
        try:
            user_choice = int(input("\033[0;94mEnter 1 for passwords or 2 for passphrases -> \033[0m"))
            if user_choice in [1,2]:
                break
            else:
                print("\033[0;91mPlease enter 1 or 2\033[0m")
                

        except ValueError:
            print("\033[0;91mInvalid input. Please enter a number.\033[0m")

    if user_choice == 1:
        padded_msg_3 = msg_3.center(columns)
        print(f"\033[1;93m{padded_msg_3}\033[0m") 
        print()
        lower = get_valid_int("\033[93mNumber of lowercase letters -> \033[0m")
        print()
        upper = get_valid_int("\033[93mNumber of uppercase letters -> \033[0m")
        print()
        punc = get_valid_int("\033[93mNumber of punctuation marks -> \033[0m")
        print()
        digt = get_valid_int("\033[93mNumber of digits -> \033[0m")
        totals = lower + upper + punc + digt
        if totals > 90:
            padded_msg_5 = msg_5.center(columns)
            print(f"\033[1;93m{padded_msg_5}\033[0m")
        generated_password = generate_password(lower, upper, punc, digt, totals)
        print()
        print(f"\033[0;39mHere is your secured password: {generated_password}\033[0m")

    if user_choice == 2:
        padded_msg_4 = msg_4.center(columns)
        print(f"\033[1;95m{padded_msg_4}\033[0m") 
        print()
        length = get_valid_int("\033[1;95mNumber of words -> \033[0m")
        generated_passphrase = random_passphrase_generator(length)
        print(f"\033[0;39mHere is your secured passphrase: {generated_passphrase}\033[0m")




def generate_password(l,u,p,d, total):
    lwr = random.choices(string.ascii_lowercase, k = l)
    uppr = random.choices(string.ascii_uppercase, k = u)
    punctuations = random.choices(string.punctuation, k = p)
    digits = random.choices(string.digits, k = d)
    alphabet = lwr + uppr + punctuations + digits
    
    while True:
        password = ''.join(random.choice(alphabet) for i in range(total))
        ispunct = total - (sum(c.isupper() for c in password) + sum(c.islower() for c in password) + sum(c.isdigit() for c in password))
        if (sum(c.islower() for c in password) == l
                and sum(c.isupper() for c in password) == u
                and sum(c.isdigit() for c in password) == d
                and (ispunct == p)) :
            break
    return password

def random_passphrase_generator(word_count):
    # Get the directory where this Python file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    word_list_path = os.path.join(current_dir, 'word_list.txt')
    
    with open(word_list_path) as f:
        #words list is taken from here https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases
        words = [word.strip() for word in f]
        passphrase = ' '.join(secrets.choice(words) for i in range(word_count))
        f.close()
    return passphrase

def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
            if type(lower) == int:
                break
        except ValueError:
            print("\033[0;91mInvalid input. Please enter a number.\033[0m")

if __name__ == "__main__":
    main()