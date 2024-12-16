# Exibe uma arte inicial no jogo
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Exibe a mensagem de boas-vindas ao jogador
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Primeira escolha: jogador escolhe para onde ir
choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

# Validação da primeira escolha
while choice1 not in ["left", "right"]:
    print("Invalid choice. Please type 'left' or 'right'.")
    choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

# Se o jogador escolher "left", o jogo prossegue, caso contrário, termina
if choice1 == "left":
    # Segunda escolha: jogador decide o que fazer ao chegar no lago
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()

    # Validação da segunda escolha
    while choice2 not in ["wait", "swim"]:
        print("Invalid choice. Please type 'wait' or 'swim'.")
        choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()

    # Se o jogador escolher "wait", o jogo continua, caso contrário, termina
    if choice2 == "wait":
        # Terceira escolha: jogador escolhe uma das portas
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()

        # Validação da terceira escolha
        while choice3 not in ["red", "yellow", "blue"]:
            print("Invalid choice. Please choose 'red', 'yellow', or 'blue'.")
            choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()

        # O que acontece dependendo da escolha da porta
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")  # Se o jogador escolhe a porta vermelha, ele morre
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")  # Se o jogador escolhe a porta amarela, ele encontra o tesouro
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")  # Se o jogador escolhe a porta azul, ele morre
    else:
        print("You get attacked by an angry trout. Game Over.")  # Se o jogador escolhe nadar, ele é atacado por uma truta furiosa
else:
    print("You fell into a hole. Game Over.")  # Se o jogador escolhe a direção "right", ele cai em um buraco

