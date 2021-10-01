def check(tickets):
    winners_list = []
    for ticket in tickets:
        if len(ticket.numbers) == 0:
            winners_list.append(ticket)
    return winners_list

def print_winners_list(winners_list):
    print("\n")
    print("BINGO! Tenemos ganador/es:")
    for winner in winners_list:
        print(winner)