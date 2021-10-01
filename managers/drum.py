import random

def init():
    rotating_drum = list(range(1,91))
    random.shuffle(rotating_drum)
    return rotating_drum

def pull_ball(rotating_drum):
    return rotating_drum.pop(0)

def next_ball(rotating_drum):
    if (len(rotating_drum) != 0):
            input("Pulsa para extraer la siguiete bola:\n")

def endgame():
    print("Bombo vacío! Fin del juego")