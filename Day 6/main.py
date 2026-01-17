from input import puzzleinput
#from testinput import puzzleinput

question_part = 2

### Part one

def input_into_individual_problems(input: str) -> list[list[str]]:
    rows = input.split("\n")
    new_rows = []
    for row in rows:
        new_row = row.split()
        new_rows.append(new_row)
    problems = []
    for i in range(0, len(new_rows[0])):
        problem = []
        for row in new_rows:
            problem.append(row[i])
        problems.append(problem)
    return problems  

def calculate_problem(problem: list[str]) -> int:
    opr = problem[-1]
    result = 0
    if opr == "*":
        result = 1
    for i in range(0, len(problem) - 1):
        equation = f"{result} {opr} {problem[i]}"
        result = eval(equation)
    return result


def calculate_all_problems(problems: list[list[str]]) -> int:
    result = 0
    for problem in problems:
        result += calculate_problem(problem)
    return result

### Part Two

def input_into_cephalopod_problems(input:str) -> list[list[str]]:
    rows = input.split("\n")
    row_count = len(rows)
    working_data = rows[:]
    ceph_problems = []
    more_problems = True
    while more_problems:
        try:
            lengths = []
            problem = []
            for i in range(0, row_count - 1):
                lengths.append(working_data[i].index(" "))
            length = max(lengths)
            for i in range(0, row_count):
                problem.append(working_data[i][:length])
            ceph_problems.append(problem)
            for i in range(0, row_count):
                working_data[i] = working_data[i][length + 1:]
        except ValueError:
            more_problems = False
            problem = []
            for i in range(0, row_count):
                problem.append(working_data[i])
            ceph_problems.append(problem)
    return ceph_problems
    
def calculate_ceph_problem(problem: list[str]) -> int:
    opr = problem[-1].strip()
    result = 0
    if opr == "*":
        result = 1
    ceph_numbers = []
    for d in range(len(problem[0]) - 1, -1, -1):
        digit_list = []
        for r in range(0, len(problem) - 1):
            digit_list.append(problem[r][d].strip())
        number = int("".join(digit_list))
        ceph_numbers.append(number)
    for i in range(0, len(ceph_numbers)):
        equation = f"{result} {opr} {ceph_numbers[i]}"
        result = eval(equation)
    return result

def calculate_all_ceph_problems(problems: list[list[str]]) -> int:
    result = 0
    for problem in problems:
        result += calculate_ceph_problem(problem)
    return result

### Main

def main():
    problems = []
    results = 0
    if question_part == 1:
        problems = input_into_individual_problems(puzzleinput)
        results = calculate_all_problems(problems)
    if question_part == 2:
        problems = input_into_cephalopod_problems(puzzleinput)
        results = calculate_all_ceph_problems(problems)
    print("Answer: ", results)

if __name__=="__main__":
    main()

