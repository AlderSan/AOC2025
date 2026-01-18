from input import puzzleinput
#from testinput import puzzleinput
import math
import sys

question_part = 2
#list 1 - list_of_boxes
#list 2 - reference list of (box index, closest box index, distance) - SORTED
#list 3 - list of circuits (sets)

#list of circuits -> set to prevent duplicates?
#are they connected -> are both boxes found in the same index (set) in the list of circuits?
#if they are not connected - combine set B to set A

#test - make 10 connections
#actual - make 1000 connections

#make second list - matches first list index, finding closest box and storing index and distance

def input_into_box_tuples(input: str) -> list[tuple[int, int, int]]:
    str_list = input.split("\n")
    tuple_list = []
    for str in str_list:
        list_of_coord = str.split(",")
        box = (int(list_of_coord[0]), int(list_of_coord[1]), int(list_of_coord[2]))
        tuple_list.append(box)
    return tuple_list


def distance_between(box1: tuple[int, int, int], box2: tuple[int, int, int]) -> float:
    return math.dist(box1, box2)

def calc_results(list_of_circuits) -> int:
    return len(list_of_circuits[0]) * len(list_of_circuits[1]) * len(list_of_circuits[2])


def make_list_of_circuits(list_of_boxes: list[tuple[int, int, int]]) -> list[set[tuple[int, int, int]]]:
    circuit_list = []
    for box in list_of_boxes:
        circuit_list.append({box})
    return circuit_list


def create_list_of_merges(list_of_boxes):
    merge_list = []
    for box1 in list_of_boxes:
        for box2 in list_of_boxes:
            if box1 != box2:
                merge_list.append((box1, box2, distance_between(box1, box2)))
    sorted_list = sorted(merge_list, key=lambda tup: tup[2])
    return sorted_list


def find_index_in_circuits(box1, list_of_circuits: list[set[tuple[int,int,int]]]) -> int:
    for circuit in list_of_circuits:
        if box1 in circuit:
            return list_of_circuits.index(circuit)
    raise Exception("not found in circuits")


def make_connection(box1_index: int, box2_index: int, list_of_circuits: list[set[tuple[int, int, int]]]) -> list[set[tuple[int,int,int]]]:
    list_of_circuits[box1_index].update(list_of_circuits[box2_index])
    del list_of_circuits[box2_index]
    return list_of_circuits


def process_closest_list(closest_list: list[tuple[tuple[int, int, float], tuple[int, int, int], float]], list_of_circuits: list[set[tuple[int, int, int]]]) ->  list[set[tuple[int, int, int]]]:
    merged_circuits = list_of_circuits[:]
    for merge in closest_list:
        box1 = merge[0]
        box2 = merge[1]
        box1_index = find_index_in_circuits(box1, merged_circuits)
        box2_index = find_index_in_circuits(box2, merged_circuits)
        if box1_index != box2_index:
            merged_circuits = make_connection(box1_index, box2_index, merged_circuits)
    return sorted(merged_circuits, key=len, reverse=True)

def process_closest_list_part_2(closest_list: list[tuple[tuple[int, int, float], tuple[int, int, int], float]], list_of_circuits: list[set[tuple[int, int, int]]]):
    merged_circuits = list_of_circuits[:]
    box1 = tuple()
    box2 = tuple()
    while len(merged_circuits) != 1:
        for merge in closest_list:
            box1 = merge[0]
            box2 = merge[1]
            box1_index = find_index_in_circuits(box1, merged_circuits)
            box2_index = find_index_in_circuits(box2, merged_circuits)
            if box1_index != box2_index:
                merged_circuits = make_connection(box1_index, box2_index, merged_circuits)
            if len(merged_circuits) == 1:
                break
    return box1, box2

def calculate_part_2_result(box1, box2):
    box1_x = box1[0]
    box2_x = box2[0]
    return box1_x * box2_x



def main():
    box_list = input_into_box_tuples(puzzleinput)
    closest_list = create_list_of_merges(box_list)
    result=0
    if question_part == 1:
        if len(sys.argv) > 1:
            connections = int(sys.argv[1])
        else:
            connections = 10
        closest_list = closest_list[:connections * 2]
    closest_list = closest_list[::2]
    circuit_list = make_list_of_circuits(box_list)
    if question_part == 1:
        processed_list = process_closest_list(closest_list, circuit_list)
        result = calc_results(processed_list)
    if question_part == 2:
        final_box1, final_box2 = process_closest_list_part_2(closest_list, circuit_list)
        result = calculate_part_2_result(final_box1, final_box2)

    print("Answer: ",result)


if __name__ == "__main__":
    main()

