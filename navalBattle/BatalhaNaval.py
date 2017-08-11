'''
Created on 11 de ago de 2017

@author: Bruno Queiroz
'''
from random import randint

if __name__ == '__main__':
    pass



board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

op = 0
while(op >3 or op<1):
    print("Qual dificuldade?\n1-Facil(9 turnos)\n2-Medio(6 turnos)\n3-Dificil(4 turnos)")
    op = int(input("opcao: "))

    if op == 1:
        turnos = 9
    elif op == 2:
        turnos = 6
    elif op == 3:
        turnos = 4
    else:
        print("\n\nDigite um numero valido!!")


print ("Vamos jogar Batalha Naval!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(turnos):
    guess_row = int(input("Adivinhe a Linha:"))
    guess_col = int(input("Adivinhe a Coluna:"))

    if (guess_row - 1) == ship_row and (guess_col - 1) == ship_col:
        print ("Parabens, voce afundou meu couracado!")
        break
    else:
        if ((guess_row - 1) < 0 or (guess_row - 1) > 4) or ((guess_col - 1) < 0 or (guess_col - 1) > 4):
            print ("\n\nOops, isso nao e nem mesmo no oceano.")
        elif(board[guess_row - 1][guess_col - 1] == "X"):
            print ("\n\nJoce ja tentou esse.")
        else:
            print ("\n\nVoce errou meu couracado!")
            board[guess_row - 1][guess_col - 1] = "X"
        if turn == (turnos-1):
            print ("\n\nGame Over")
    print ("Turn", turn + 1)
    print_board(board)
