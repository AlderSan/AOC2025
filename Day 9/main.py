from input import puzzleinput
#from testinput import puzzleinput

question_part = 1

def calc_area(corner1: tuple[int, int], corner2: tuple[int, int]) -> int:
    x1, y1 = corner1
    x2, y2 = corner2
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

def input_to_corners(input: str) -> list[tuple[int, int]]:
    list_lists = input.split("\n")
    corners_list = []
    for list in list_lists:
        split_list = list.split(",")
        corners_list.append((int(split_list[0]),int(split_list[1])))
    return corners_list

def find_largest_area(list_of_corners: list[tuple[int, int]]) -> int:
    largest_area_so_far = 0
    for corner1 in list_of_corners:
        for corner2 in list_of_corners:
            area = calc_area(corner1, corner2)
            if area > largest_area_so_far:
                largest_area_so_far = area
    return largest_area_so_far

def main():
    red_tiles_list = input_to_corners(puzzleinput)
    result = find_largest_area(red_tiles_list)
    print("Answer: ", result)

if __name__ == "__main__":
    main()



