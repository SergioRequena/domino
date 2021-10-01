from constants import colors as color
from constants import formats as format

def init(rows, columns):
    matrix = []
    for i in range(rows):
        a = ["**"]*columns
        matrix.append(a)
    return matrix

def update(matrix, ball):
    row = ball//10
    column = ball%10
    if column == 0:
        row = row - 1
        column = 9
    else:
        column = column - 1
    matrix[row][column] = ball

def draw(matrix, ball):
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