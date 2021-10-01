import json

from classes.Ticket import Ticket

def load():
    tickets = []
    with open('D:/Python/lotobingo/data/tickets.json') as json_file:
        data = json.load(json_file)
        for ticket in data['tickets']:
            new_ticket = Ticket(ticket["id"],ticket["colour"],ticket["numbers"],0)
            tickets.append(new_ticket)
    return tickets

def update(tickets, ball):
    for ticket in tickets:
        for number in ticket.numbers:
            if int(number) == ball:
                ticket.numbers.remove(number)