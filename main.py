from managers import tickets
from managers import grid
from managers import drum
from managers import winner

def main():
    tickets_list = tickets.load()
    matrix = grid.init(9,10)
    rotating_drum = drum.init()
    winners_list = []
    while len(rotating_drum) > 0 and len(winners_list) == 0:
        ball = drum.pull_ball(rotating_drum)
        grid.update(matrix, ball)
        grid.draw(matrix, ball)
        tickets.update(tickets_list, ball)
        winners_list = winner.check(tickets_list)
        if len(winners_list) == 0:
            input("Pulsa para extraer la siguiete bola:\n")
    winner.print_winners_list(winners_list)

if __name__ == "__main__":
    main()