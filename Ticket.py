class Ticket:
    def __init__(self, id, colour, numbers):
        self.id = id
        self.colour = colour
        self.numbers = []
        
        for number in numbers.split(","):
            self.numbers.append(number)
    
    def __repr__(self):
        string = "\n"
        string += "id: " + str(self.id) + "\n"
        string += "colour: " + self.colour + "\n"
        for number in self.numbers:
            string += str(number) + " "
        return string