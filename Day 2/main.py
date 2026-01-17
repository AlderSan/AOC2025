from input import puzzleinput
#from testinput import puzzleinput

#ids are (firstid)-(lastid) separated by commas
# range of ids - check all between, inclusive

#invalid Ids: 
# - leading 0
# - repeating pattern twice, 55 (5 twice), 6464 (64 twice), 123123 (123 twice) - split string in half and check?

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

def is_invalid(id: int) -> bool:
    id_string = str(id)
    half_marker = len(id_string) // 2
    return id_string[:half_marker] == id_string[half_marker:]

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
