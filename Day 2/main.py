from input import puzzleinput
#from testinput import puzzleinput


question_part = 2

def input_to_id_pair(input: str) -> list[str]:
    return input.split(",")

def id_pair_to_list(id_pair: str) -> list[int]:
    split_pair = id_pair.split("-")
    first_id = int(split_pair[0])
    last_id = int(split_pair[1])
    list_of_ids = []
    for i in range(first_id, last_id + 1):
        list_of_ids.append(i)
    return list_of_ids

def split_string_every_n(string: str, n: int) -> list[str]:
    splits = []
    for i in range(0, len(string), n):
        splits.append(string[i:i+n])
    return splits

def is_invalid(id: int) -> bool:
    id_string = str(id)
    invalid = False
    global question_part
    half_marker = len(id_string) // 2
    if question_part == 1:
        invalid = id_string[:half_marker] == id_string[half_marker:]
    if question_part == 2:
        for i in range(1,half_marker + 1):
            splits = split_string_every_n(id_string, i)
            invalid = len(set(splits)) <= 1
            if invalid:
                break
    return invalid


def count_invalid(id_list: list[int]) -> int:
    invalid_count = 0
    for id in id_list:
        if is_invalid(id):
            invalid_count += id
    return invalid_count

def main():
    id_pairs = input_to_id_pair(puzzleinput)
    invalid_count = 0
    for id_pair in id_pairs:
        id_list = id_pair_to_list(id_pair)
        invalid_count += count_invalid(id_list)
    print("Answer: ", invalid_count)

if __name__ == "__main__":
    main()
