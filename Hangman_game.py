from string import punctuation
from random import randint

def welcome():
    with open("./archivos/welcome_mes.txt", "r", encoding='utf-8') as f:
        for line in f:
            print(line, end='')

def user_input():
    """Acá recibimos la entrada del usuario y verificamos
    que sea una sola letra

    Raises:
        TypeError: [Le mostramos al usuario que solo se puede
                    ingresar un caracter y debe ser una letra]
    """
    while True:
        try:
            letter = input('type a letter: ') # get a input from user
            if len(letter) != 1 or letter.isdigit() or punctuation.find(letter) >= 0:
                raise TypeError
            break
        except TypeError:
            print("Only enter a letter")
    return letter



def load_word_2dict():
    """En esta función se carga el data para generar un diccionario de la
        de arrays y "facilitar" la comparación de letras
    """
    count = 0
    my_dict = {}
    with open("./archivos/data.txt", "r", encoding='utf-8') as f:
        for line in f:
            temp = line.maketrans("áéíóú","aeiou")
            line = line.strip("\n").translate(temp)
            my_dict[count] = line
            count += 1
    f.close()
    return my_dict

def compare_dict_input(choosed_word, user_in, user_word, hearts):
    index = 0
    found = False
    for i in range(len(choosed_word)):
        index = choosed_word.find(user_in, index)
        if index >= 0:
            user_word[index] = user_in
            index += 1
            found = True
        else:
            break
    if not found:
        hearts -= 1
        print("any")

    return user_word, hearts

def new_game(my_dict):
    user_word =[]
    choosed_word = my_dict[randint(0, len(my_dict))]
    hearts = 5

    welcome()
    print("\n")

    for underscore in range(len(choosed_word)):
        user_word.append("_ ")

    return user_word, choosed_word, hearts

def ui(user_word, hearts):
    for i in range(len(user_word)):
        print(user_word[i], end=" ")

    for i in range(0, hearts):
        print("♥", end="")
    print("\n")

def start_again(my_dict):
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        user_word, choosed_word, hearts = new_game(my_dict)
    else:
        print("good bye")
        play_again = 0
        return 0, '', '', 1
    return play_again, user_word, choosed_word, hearts

def run():
    my_dict = load_word_2dict()
    play_again = 1
    user_word, choosed_word, hearts = new_game(my_dict)

    while play_again:
        ui(user_word,hearts)
        user_in = user_input()
        user_word, hearts = compare_dict_input(choosed_word, user_in, user_word, hearts)

        if user_word == [i for i in choosed_word]:
            for i in user_word:
                print(i, end=" ")
            print("\n", "You Won!", "\n")
            play_again, user_word, choosed_word, hearts = start_again(my_dict)

        if not hearts:
            print("you loose")
            print(choosed_word)
            play_again, user_word, choosed_word, hearts = start_again(my_dict)
            return
    return

if __name__ == '__main__':
    run()


