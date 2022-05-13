import os
from operator import truediv
from random import randint

# Lee el archivo data.txt y lo retorna en una lista
def read():
    words_txt = []
    with open("./datos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words_txt.append(line.replace("\n", ""))
    return words_txt

# Imprime la bienvenida
def imprimir_bienvenida():
    print("Bienvenidos al juego\nA continuación se elegirá una palabra aleatoriamente\nDebe adivinar la palabra letra por letra")
    print("Solo debe ingresar letras en minúscula")

# Limpia la pantalla e imprime la interface del juego
def interface(list_word, num_intentos=0):
    os.system("cls") #limpia la pantalla
    word = ""
    for letter in list_word:
        word = word + letter + " "
    print(word + "     " + str(num_intentos))

# Lee la lista de palabras y elige una aleatoriamente
def seleccion_palabra():
    words = read()
    num = randint(0, len(words))
    return words[num]

def run():
    word = seleccion_palabra()
    word_list_tuple = list(enumerate(word))
    word_list = ["_" for letter in word]
    terminado = False
    imprimir_bienvenida()
    os.system("cls")
    hay_intentos = False
    limite_intentos = 0
    intentos = 1
    level = int(input("Ingrese el nivel que desea:\n- 1 es el nivel más fácil\n- 2 es el nivel intermedio\n- 3 es el nivel difícil\n- 123 es el nivel GOD\n"))
    assert (level >= 1 and level <= 3) or level == 123, "Por favor ingrese un nivel válido"
    if level == 1:
        hay_intentos = False
        word_list[0] = word_list_tuple[0][1]
        word_list[len(word_list) - 1] = word_list_tuple[len(word_list) - 1][1]
    elif level == 2:
        hay_intentos = True
        limite_intentos = len(word) * 3
    elif level == 3:
        hay_intentos = True
        limite_intentos = len(word) * 2
    elif level == 123:
        hay_intentos = True
        limite_intentos = len(word)
    else:
        print("\n\nAlgo está fallando y paso las pruebas")
    interface(word_list, limite_intentos)
    while not terminado and (not hay_intentos or intentos <= limite_intentos):
        try:
            
            letter_in = input("Ingrese una letra: ")
            if (ord(letter_in) > 90 and ord(letter_in) < 97) or ord(letter_in) < 65:
                raise ValueError("Por favor ingrese una letra")
            elif ord(letter_in) > 122 and ord(letter_in) != 241 and ord(letter_in) != 209:
                raise ValueError("Por favor ingrese una letra")
            elif ord(letter_in) >= 65 and ord(letter_in) <= 90:
                letter_in = chr(ord(letter_in) + 32)
            elif ord(letter_in) == 209:
                letter_in = chr(241)
            
            for t in word_list_tuple:
                if t[1] == letter_in:
                    word_list[t[0]] = t[1]
            interface(word_list, limite_intentos - intentos)
            intentos += 1
            if not ("_" in word_list):
                print("\nGanaste, la palabra era: " + word)
                terminado = True
        except ValueError as ve:
            print(ve)
    
if __name__ == '__main__':
    run()