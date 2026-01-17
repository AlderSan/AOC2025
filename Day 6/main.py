from input import puzzleinput
#from testinput import puzzleinput

question_part = 1


#problems are sorted vertically
#need to break list into rows, then create new lists from the Nth value in each row, last value is operator


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
    if opr == "*" or opr == "/":
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

def main():
    problems = input_into_individual_problems(puzzleinput)
    results = calculate_all_problems(problems)
    print("Answer: ", results)

if __name__=="__main__":
    main()

