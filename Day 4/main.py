from input import puzzleinput
#from testinput import puzzleinput

#matrix[row][column]

question_part = 2

def create_matrix_from_input(input:str) -> list[str]:
    rows = input.strip().split("\n")
    return rows

def remove_removable_rolls(matrix: list[str], list_of_removable_rolls: list[tuple[int, int]]) -> list[str]:
    new_matrix = matrix[:]
    for roll in list_of_removable_rolls:
        matrix_row = new_matrix[roll[0]] #a string
        matrix_row = list(matrix_row) #list of strings
        matrix_row[roll[1]] = "."
        matrix_row = "".join(matrix_row)
        new_matrix[roll[0]] = matrix_row
    return new_matrix


def make_adjacent_list(row: int, column: int) -> list[tuple[int, int]]:
    adjacent_list = []
    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):
            if r >= 0 and c >= 0:
                adjacent_list.append((r, c))
    adjacent_list.remove((row, column))
    return adjacent_list

#indexError
def count_adjacent(matrix:list[str], row, column) -> int:
    adjacent_list = make_adjacent_list(row, column)
    count = 0
    adjacent = []
    for location in adjacent_list:
        try:
            if matrix[location[0]][location[1]] == "@":
                count += 1
                adjacent.append(location)
        except IndexError:
            count += 0
    return count
        
def count_all_valid(matrix:list[str]): # -> int, list[tuple[int, int]]:
    total_count = 0
    removable_rolls = []
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[0])):
            if matrix[row][column] == "@":
                if count_adjacent(matrix, row, column) < 4:
                    total_count += 1
                    removable_rolls.append((row, column))
    return total_count, removable_rolls

def main():
    matrix = create_matrix_from_input(puzzleinput)
    new_matrix = matrix
    count, removable_rolls = count_all_valid(matrix)
    while question_part == 2 and removable_rolls != []:
        new_matrix = remove_removable_rolls(new_matrix, removable_rolls)
        count2, removable_rolls = count_all_valid(new_matrix)
        count += count2
    print("Answer: ", count)

if __name__ == "__main__":
    main()