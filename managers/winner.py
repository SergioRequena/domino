def check(tickets, winners_list):
    rank = len(winners_list) + 1
    for ticket in tickets:
        if len(ticket.numbers) == 0:
            ticket.update_rank(rank)
            winners_list.append(ticket)
            tickets.remove(ticket)
    return winners_list, tickets

def print_winners_list(winners_list):
    if len(winners_list) != 0:
        print("\n")
        print("BINGO! Tenemos ganador/es:")
        for winner in winners_list:
            print(winner)

def print_final_ranking(winners_list):
    print("-------------------------------")
    print("-- RANKING FINAL --------------")
    print("-------------------------------")
    for winner in winners_list:
        if winner.rank == 1:
            print("-- 1. Cartón " + str(winner.id) + " de color " + winner.colour)
            print("-------------------------------")
        if winner.rank == 2:
            print("-- 2. Cartón " + str(winner.id) + " de color " + winner.colour)
            print("-------------------------------")
        if winner.rank == 3:
            print("-- 3. Cartón " + str(winner.id) + " de color " + winner.colour)
            print("-------------------------------")
    print("\n")