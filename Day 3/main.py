from input import puzzleinput
#from testinput import puzzleinput

#input into banks (row of digits)
#from each bank - calcluate highest number from pairing the two digits IN ORDER
#calculate total joltage by adding all the banks together

def input_into_banks(input:str) -> list[str]:
    return input.strip().split("\n")

def find_max_joltage(bank:str) -> int:
    max_joltage_so_far = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(f"{bank[i]}{bank[j]}")
            max_joltage_so_far = max(max_joltage_so_far, joltage)
    return max_joltage_so_far

def sum_total_joltage(input:str) -> int:
    banks = input_into_banks(input)
    total_joltage = 0
    for bank in banks:
        total_joltage += find_max_joltage(bank)
    return total_joltage

def main():
    answer = sum_total_joltage(puzzleinput)
    print("Answer: ", answer)



if __name__ == "__main__":
    main()