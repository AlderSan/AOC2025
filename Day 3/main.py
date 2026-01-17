from input import puzzleinput
#from testinput import puzzleinput

question_part = 2
#input into banks (row of digits)
#from each bank - calcluate highest number from pairing the two digits IN ORDER
#calculate total joltage by adding all the banks together

def input_into_banks(input:str) -> list[str]:
    return input.strip().split("\n")

def find_next_highest_digit_index(bank:str, n: int, previous_index: int, n_length: int) -> int:
    highest_so_far = 0
    highest_so_far_index = 0
    start_index = previous_index + 1
    end_slice =  n - n_length
    if end_slice == 0:
        eligible_bank = bank[start_index:]
    else:
        eligible_bank = bank[start_index:end_slice]
    for digit in eligible_bank:
        if int(digit) > highest_so_far:
            highest_so_far = int(digit)
            highest_so_far_index = eligible_bank.index(digit) + start_index
    return highest_so_far_index

def find_highest_combination(bank:str) -> int:
    n_length = 2
    if question_part == 2:
        n_length = 12
    indexes = []
    previous_index = -1
    joltage = ""
    for i in range(1, n_length + 1):
        hdi = find_next_highest_digit_index(bank, i, previous_index, n_length)
        indexes.append(hdi)
        previous_index = hdi
    for index in indexes:
        joltage += str(bank[index])
    print(joltage)
    return int(joltage)

def sum_total_joltage(input:str) -> int:
    banks = input_into_banks(input)
    total_joltage = 0
    for bank in banks:
        total_joltage += find_highest_combination(bank)
    return total_joltage

def main():
    answer = sum_total_joltage(puzzleinput)
    print("Answer: ", answer)



if __name__ == "__main__":
    main()