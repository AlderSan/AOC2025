from aocd import get_data
from testinput import test_input

#automatic get from aocd
real_input = get_data(day=12, year=2025)

puzzleinput = real_input


def split_input(input: str) -> tuple[list[str], list[str]]:
    split1 = input.split("\n\n")
    raw_shapes_list:list[str] = []
    for i in range(0, len(split1)):
        if split1[i].startswith(str(i)):
            raw_shapes_list.append(split1[i])
    split_trees = split1[-1].split("\n")
    shape_list = []
    for shape in raw_shapes_list:
        new_shape = shape.split(":")
        shape_list.append(new_shape[1])
    return shape_list, split_trees

shapes, trees = split_input(puzzleinput)

#clearing out edge cases
#any where size is guaranteed to not fit
def shape_area_too_large(shapes: list[str], tree_area: str) -> bool:
    tree_size, tree_presents = tree_area.split(":")
    tree_l_w = tree_size.split("x")
    tree_area = int(tree_l_w[0]) * int(tree_l_w[1])
    presents_qty_by_index = tree_presents.split()

    present_area_by_index = []
    for shape in shapes:
        area = shape.count("#")
        present_area_by_index.append(area)
    present_area_by_index[-1] = present_area_by_index[-1] + 1
    total_present_area = 0
    for i in range(0, len(presents_qty_by_index)):
        total_present_area += int(present_area_by_index[i]) * int(presents_qty_by_index[i])
    return total_present_area < tree_area

def check_shape_area(shapes: list[str], list_of_trees: list[str]) -> list[bool]:
    check_list = []
    for tree in list_of_trees:
        check_list.append(shape_area_too_large(shapes, tree))
    enum_check_list = enumerate(check_list)
    return list(enum_check_list)

checked = check_shape_area(shapes, trees)

def clean_enum_bool_list(list_of_checked):
    cleaned_list = []
    for checked in list_of_checked:
        if checked[1]:
            cleaned_list.append(checked)
    return cleaned_list

cleaned = clean_enum_bool_list(checked)

print(len(checked))
print(len(cleaned))