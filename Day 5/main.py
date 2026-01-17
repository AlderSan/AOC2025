from input import puzzleinput
#from testinput import puzzleinput

question_part = 2

#database:
#fresh ID ranges - inclusive, may overlap
#blank line
#available ingredient IDs

#count fresh ingredients

def format_fresh_range(fresh_range:str) -> list[int]:
    range_list = fresh_range.split("-")
    full_range_list = []
    for i in range(int(range_list[0]), int(range_list[1]) + 1):
        full_range_list.append(i)
    return full_range_list

def separate_database(database: str) -> tuple[list[list[int]], list[int]]:
    temp_list = database.split("\n")
    fresh_list = []
    ingredient_id_list = []
    for item in temp_list:
        if "-" in item:
            temp = item.split("-")
            fresh_list.append([int(temp[0]),int(temp[1])])
        elif item != "":
            ingredient_id_list.append(int(item))
    return fresh_list, ingredient_id_list

def check_and_remove_overlaps(fresh_range: list[list[int]]) -> list[list[int]]:
    merged = [fresh_range[0]]

    for current_start, current_end in fresh_range[1:]:
        last_merged_end = merged[-1][1]
        if current_start <= last_merged_end or current_start == last_merged_end + 1:
            merged[-1][1] = max(last_merged_end, current_end)
        else:
            merged.append([current_start, current_end])
    return merged
        


def count_fresh_ids(fresh_range: list[list[int]]) -> int:
    count = 0
    for fr in fresh_range:
        count += 1 + fr[1] - fr[0]
    return count

def check_if_fresh(ingredient_id: int, fresh_range: list[list[int]]) -> bool:
    is_fresh = False
    for fr in fresh_range:
        if ingredient_id in range(fr[0], fr[1] + 1):
            is_fresh = True
    return is_fresh

def main():
    fresh_range, ingredient_id_list = separate_database(puzzleinput)
    fresh_range = sorted(fresh_range)
    merged_fr = check_and_remove_overlaps(fresh_range)
    count = 0
    if question_part == 1:
        for ingredient_id in ingredient_id_list:
            if check_if_fresh(ingredient_id, merged_fr):
                count += 1
    if question_part == 2:
        count = count_fresh_ids(merged_fr)
    print("Answer: ", count)

if __name__ == "__main__":
    main()