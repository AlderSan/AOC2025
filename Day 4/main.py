from input import puzzleinput
#from testinput import puzzleinput

#matrix[row][column]

def create_matrix_from_input(input:str) -> list[str]:
    rows = input.strip().split("\n")
    return rows




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
        
def count_all_valid(matrix:list[str]) -> int:
    total_count = 0
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[0])):
            if matrix[row][column] == "@":
                if count_adjacent(matrix, row, column) < 4:
                    total_count += 1
    return total_count

def main():
    matrix = create_matrix_from_input(puzzleinput)
    count = count_all_valid(matrix)
    print(count)

if __name__ == "__main__":
    main()