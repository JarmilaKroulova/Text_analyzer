"""
author: Jarmila Kroulová
email: jarmilxxx@seznam.cz
"""


from main_data import texts, register_users


def process_user_input(texts, register_users):
    """
    Zpracuje vstupy od uživatele, zkontroluje zda je uživatel registrován,
    pokud ano přivítá jej a nabídne výběr textu k analýze, 
    pokud není registrován, ukončí program.
    Parametry: texts = list textů k analýze
            register_users = slovník uživatelů s jejich hesly
    Vrací: zvolený text (víceřádkový string)
    """
    separator = "-" *40 
    print(f"{separator}\n If you are using the text analyzer app,\nplease enter your username and password.\n{separator}")
    number_of_texts = len(texts)
    user = input("username: ").lower().strip()
    password = input("password: ").lower().strip()

    if user in register_users and password == register_users[user]:
        print(f"{separator}\n Welcome to the app, {user}\n We have {number_of_texts} texts to be analyzed.\n{separator}")
    else:
        print("Unregistered user, terminating the program.")
        quit()
    # text selection
    for _ in range(number_of_texts):
        selected_text = input(f"Enter a number btw. 1 and {number_of_texts} to select: ").strip()
        if selected_text.isdigit():
            choice = int(selected_text)
            if 0 < choice <= number_of_texts:
                text = texts[choice-1]
                print(f"{separator}\n You have selected text number '{choice}' for analysis.\n{separator}")
                return text
                break
            else:
                print("Try again! This is not in correct range.")
        else:
            print("Try again! This is not a number.")
    else:
        print(f"{separator}\nYou are failed. Terminating program.\n{separator}")
        quit()


def process_text(text):
    """
    Analyzuje text
    Parametry: text = zvolený text k analýze (víceřádkový string)
    Vrací: výsledky v proměnných a jeden slovník
    """
    pure_word = [word.strip(" ,.:?!") for word in text.split()]
    # word division
    titlecase = []
    uppercase = []
    lowercase = [] 
    numbers = []
        
    for word in pure_word: 
        if word.istitle():
            titlecase.append(word)
        elif word.isupper():
            uppercase.append(word)
        elif word.islower():
            lowercase.append(word)
        if word.isnumeric():
            numbers.append(int(word))
    # number of words
    number_of_words = len(pure_word)
    is_titlecase = len(titlecase)
    is_uppercase = len(uppercase)
    is_lowercase = len(lowercase)
    is_number = len(numbers)
    total = sum(numbers)

    length_of_words = [len(word) for word in pure_word]
    length_dictionary = {}
    for length in set(length_of_words):
        length_dictionary[length] = length_of_words.count(length)
    return number_of_words, is_titlecase, is_uppercase, is_lowercase, is_number, total, length_dictionary


def print_the_results(number_of_words, is_titlecase, is_uppercase, is_lowercase, is_number, total, length_dictionary):
    """
    Vytiskne výsledky
    Parametry: number_of_words, is_titlecase, is_uppercase, is_lowercase, is_number, total (proměnné s počty slov)
            length_dictionary (slovník s počtem a délkou slov)
    """
    separator = "-" *40 
    print(f"There are {number_of_words} words in the selected text.")
    print(f"There are {is_titlecase} titlecase words.")
    print(f"There are {is_uppercase} uppercase words.")
    print(f"There are {is_lowercase} lowercase words.")
    print(f"There are {is_number} numeric strings.")
    print(f"The sum of all the numbers {total}.")
    print(f"{separator}\nLEN|  OCCURENCES                    |NR\n{separator}")

    for row in length_dictionary.items():
        len, occurences = row
        if occurences > 0:
            print(f"{len:<2} | {'*' * int(occurences):<30} | {occurences}")


def text_analyzer():  
    """
    Hlavní funkce textového analyzéru
    """ 
    
    text = process_user_input(texts, register_users)
    number_of_words, is_titlecase, is_uppercase, is_lowercase, is_number, total, length_dictionary = process_text(text)
    print_the_results(number_of_words, is_titlecase, is_uppercase, is_lowercase, is_number, total, length_dictionary)


if __name__ == "__main__":
    text_analyzer()  

