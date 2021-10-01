import random
import json

from classes.Ticket import Ticket
from constants import colors as color
from constants import formats as format

def main():
    tickets = load_tickets()
    matrix = init_grid(9,10)
    rotating_drum = init_rotating_drum()
    winners_list = []
    while len(rotating_drum) > 0 and len(winners_list) == 0:
        ball = pull_ball(rotating_drum)
        update_matrix(matrix, ball)
        draw_grid(matrix, ball)
        update_tickets(tickets, ball)
        winners_list = check_winner(tickets)
        input("Pulsa para extraer la siguiete bola:\n")
    print_winners_list(winners_list)

def init_grid(rows, columns):
    matrix = []
    for i in range(rows):
        a = ["**"]*columns
        matrix.append(a)
    return matrix

def init_rotating_drum():
    rotating_drum = list(range(1,91))
    random.shuffle(rotating_drum)
    return rotating_drum

def pull_ball(rotating_drum):
    return rotating_drum.pop(0)

def update_matrix(matrix, ball):
    row = ball//10
    column = ball%10
    if column == 0:
        row = row - 1
        column = 9
    else:
        column = column - 1
    matrix[row][column] = ball

def draw_grid(matrix, ball):
    print("---------------------------------------------------")
    for row in matrix:
        string = "|"
        for column in row:
            if column == ball:
                string += format.BOLD + color.GREEN + " " + str(column).zfill(2) + color.WHITE + " |"
            elif column != "**":
                string +=  color.CYAN + " " + str(column).zfill(2) + color.WHITE + " |"
            else:
                string += " " + str(column).zfill(2) + " |"
        print(string)
        print("---------------------------------------------------")

def load_tickets():
    tickets = []
    with open('D:/Python/lotobingo/data/tickets.json') as json_file:
        data = json.load(json_file)
        for ticket in data['tickets']:
            new_ticket = Ticket(ticket["id"],ticket["colour"],ticket["numbers"])
            tickets.append(new_ticket)
    return tickets

def update_tickets(tickets, ball):
    for ticket in tickets:
        for number in ticket.numbers:
            if int(number) == ball:
                ticket.numbers.remove(number)

def check_winner(tickets):
    winners_list = []
    for ticket in tickets:
        if len(ticket.numbers) == 0:
            winners_list.append(ticket)
    return winners_list

def print_winners_list(winners_list):
    for winner in winners_list:
        print(winner)

if __name__ == "__main__":
    main()