import random

def init():
    rotating_drum = list(range(1,91))
    random.shuffle(rotating_drum)
    return rotating_drum

def pull_ball(rotating_drum):
    return rotating_drum.pop(0)