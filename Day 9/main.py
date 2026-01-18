from input import puzzleinput
#from testinput import puzzleinput
from shapely.geometry import Polygon
from shapely import covered_by

question_part = 2

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

def opposite_corners(corner1: tuple[int, int], corner2: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    x1, y1 = corner1
    x2, y2 = corner2
    corner3 = (x1, y2)
    corner4 = (x2, y1)
    return corner3, corner4

def find_largest_in_polygon(list_of_corners: list[tuple[int, int]], polygon: Polygon) -> int:
    largest_area_so_far = 0
    for corner1 in list_of_corners:
        for corner2 in list_of_corners:
            corner3, corner4 = opposite_corners(corner1, corner2)
            rectangle = Polygon([corner1, corner3, corner2, corner4])
            if covered_by(rectangle, polygon):
                area = calc_area(corner1, corner2)
                if area > largest_area_so_far:
                    largest_area_so_far = area
    return largest_area_so_far


def main():
    red_tiles_list = input_to_corners(puzzleinput)
    result = 0
    if question_part == 1:
        result = find_largest_area(red_tiles_list)
    if question_part == 2:
        polygon = Polygon(red_tiles_list)
        result = find_largest_in_polygon(red_tiles_list, polygon)
    print("Answer: ", result)

if __name__ == "__main__":
    main()



