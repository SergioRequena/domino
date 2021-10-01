from managers import tickets
from managers import grid
from managers import drum
from managers import winner

def main():
    tickets_list = tickets.load()
    matrix = grid.init(9,10)
    rotating_drum = drum.init()
    winners_list = []
    while len(rotating_drum) > 0:
        ball = drum.pull_ball(rotating_drum)
        grid.update(matrix, ball)
        grid.draw(matrix, ball)
        tickets.update(tickets_list, ball)
        winners_list, ticket_list = winner.check(tickets_list, winners_list)
        winner.print_winners_list(winners_list)
        drum.next_ball(rotating_drum)
    winner.print_final_ranking(winners_list)
    drum.endgame()

if __name__ == "__main__":
    main()