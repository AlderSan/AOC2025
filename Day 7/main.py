from input import puzzleinput
#from testinput import puzzleinput

question_part = 2

def input_into_tree_list(tree: str) -> list[str]:
    return tree.split("\n")

def display_tree(tree: list[str]) -> None:
    for row in tree:
        print(row)
    print("\n")
    return

def next_laser(tree: list[str], current: int) -> tuple[list[str], int]:
    current_row = tree[current]
    next_row = tree[current + 1]
    first_i = current_row.index("|")
    count = 0
    for i in range(first_i, len(current_row)):
        
        if current_row[i] == "|" and next_row[i] == "^":
            next_row = next_row[:i-1] + "|^|" + next_row[i+2:]
            count += 1
        elif current_row[i] == "|" and next_row[i] == ".":
            next_row = next_row[:i] + "|" + next_row[i+1:]
        try:
            next = current_row[i+1:].index("|")
        except ValueError:
            break
    next_tree = tree[:]
    next_tree[current + 1] = next_row
    return next_tree, count

#too slow
def trace_laser_path_r(tree: list[str], current: tuple[int, int]) -> int:
    current_row = current[0]
    current_index = current[1]
    print_row = tree[current_row]
    print_row = print_row[:current_index] + "|" + print_row[current_index+1:]
    print(print_row)
    count = 0
    if current_row + 1 > len(tree) - 1:
        print("")
        return 1
    if tree[current_row + 1][current_index] == "^":
        count1 = trace_laser_path_r(tree, (current_row + 1, current_index - 1))
        count2 = trace_laser_path_r(tree, (current_row + 1, current_index + 1))
        count = count1 + count2
    elif tree[current_row + 1][current_index] == ".":
        count = trace_laser_path_r(tree, (current_row + 1, current_index))
    return count         

def calc_path(tree: list[str]) -> int:
    calced_tree: list[list[int]]= []
    for r in range(0, len(tree) - 1):
        if r == 0: 
            new_row = (list(map(int, list(tree[r].replace(".", "0").replace("S", "1")))))
        else:
            row = list(tree[r]) #make the current row of tree into list
            new_row = [0] * len(row)
            for i in range(0, len(row)):
                if row[i] == ".": #if it is a ".", carry item down from above 
                    new_row[i] = new_row[i] + calced_tree[r-1][i]
                if row[i] == "^": #if it is a ^, add number above to left number, i = 0, right number is set to above number)
                    new_row[i-1] = new_row[i-1] + calced_tree[r-1][i]
                    new_row[i] = 0
                    new_row[i+1] = calced_tree[r-1][i]
        calced_tree.append(new_row)
    return sum(calced_tree[-1])



def first_laser(tree: list[str]) -> list[str]:
    index = tree[0].index("S")
    next_tree = tree[:]
    next_tree[1] = next_tree[1][:index] + "|" + next_tree[1][index+1:]
    return next_tree


def main():
    tree = input_into_tree_list(puzzleinput)
    next_tree = first_laser(tree)
    count = 0
    if question_part == 1:
        for row in range(1, len(tree) - 1):
            next_tree, next_count = next_laser(next_tree, row)
            count += next_count
    if question_part == 2:
        #count = trace_laser_path_r(next_tree, (1, next_tree[1].index("|")))
        count = calc_path(tree)
    print("Answer: ", count)

if __name__ == "__main__":
    main()