from input import puzzleinput
#from testinput import puzzleinput

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

def separate_database(database: str) -> tuple[list[tuple[int, int]], list[int]]:
    temp_list = database.split("\n")
    fresh_list = []
    ingredient_id_list = []
    for item in temp_list:
        if "-" in item:
            temp = item.split("-")
            fresh_list.append((int(temp[0]),int(temp[1])))
        elif item != "":
            ingredient_id_list.append(int(item))
    return fresh_list, ingredient_id_list

def check_if_fresh(ingredient_id: int, fresh_range: list[tuple[int, int]]) -> bool:
    is_fresh = False
    for fr in fresh_range:
        if ingredient_id in range(fr[0], fr[1] + 1):
            is_fresh = True
    return is_fresh

def main():
    fresh_range, ingredient_id_list = separate_database(puzzleinput)
    count = 0
    for ingredient_id in ingredient_id_list:
        if check_if_fresh(ingredient_id, fresh_range):
            count += 1
    print("Answer: ", count)

if __name__ == "__main__":
    main()