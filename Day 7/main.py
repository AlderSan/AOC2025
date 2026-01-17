from input import puzzleinput
#from testinput import puzzleinput

question_part = 1

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

def first_laser(tree: list[str]) -> list[str]:
    index = tree[0].index("S")
    next_tree = tree[:]
    next_tree[1] = next_tree[1][:index] + "|" + next_tree[1][index+1:]
    return next_tree


def main():
    tree = input_into_tree_list(puzzleinput)
    display_tree(tree)
    next_tree = first_laser(tree)
    count = 0
    for row in range(1, len(tree) - 1):
        next_tree, next_count = next_laser(next_tree, row)
        count += next_count
    display_tree(next_tree)
    print("Answer: ", count)

if __name__ == "__main__":
    main()