class Ticket:
    def __init__(self, id, colour, numbers, rank):
        self.id = id
        self.colour = colour
        self.numbers = []
        self.rank = rank
        
        for number in numbers.split(","):
            self.numbers.append(number)
    
    def __repr__(self):
        string = "\n"
        string += "id: " + str(self.id) + "\n"
        string += "colour: " + self.colour + "\n"
        string += "rank: " + str(self.rank) + "\n"
        for number in self.numbers:
            string += str(number) + " "
        return string
    
    def update_rank(self, rank):
        self.rank = rank