#from input import puzzleinput
#from testinput2 import puzzleinput
from testinput import puzzleinput
from itertools import combinations, combinations_with_replacement
from functools import cache

question_part = 2

class Machine:
    light_sequence:str
    joltage_sequence: list[int]
    list_buttons: list[str]
    shortest_light_solution: list[str]
    shortest_joltage_solution: int

    def __init__(self, light_sequence:str, list_buttons: list[str], joltage:str)-> None:
        self.light_sequence = light_sequence
        self.list_buttons = list_buttons
        self.joltage_sequence = list(map(int,joltage.replace("{","").replace("}","").split(",")))
        print(self.joltage_sequence)
        self.find_shortest_light_solution()
        self.shortest_joltage_solution = self.find_shortest_joltage_solution(self.joltage_sequence)

    
    def is_solution(self, sequence: str, list_of_button_presses: list[str]) -> bool:
        temp_light_sequence = "".join(["." * len(sequence)])
        for button_press in list_of_button_presses:
            button = button_press[1:-1]
            button = button.replace(",", "")
            for char in button:
                num = int(char)
                if temp_light_sequence[num] == ".":
                    temp_light_sequence = temp_light_sequence[:num] + "#" + temp_light_sequence[num + 1:]
                elif temp_light_sequence[num] == "#":
                    temp_light_sequence = temp_light_sequence[:num] + "." + temp_light_sequence[num + 1:]
        return temp_light_sequence == sequence
    
    
    def find_valid_combos(self, sequence:str, current_joltage:list[int] | None = None) -> list[list[str]]:
        combos = []
        if all(char == "." for char in sequence):
            return combos
        for l in range(1, len(self.list_buttons) + 1):
            combos.extend(list(map(list,combinations(self.list_buttons, l))))
        sorted_combos = sorted(combos, key=len)
        valid_combos = list(filter(lambda c: self.is_solution(sequence, c), sorted_combos))
        if current_joltage is not None:
            for combo in valid_combos:
                press_joltage = self.press_buttons_joltage(current_joltage, combo)
                if any(digit < 0 for digit in press_joltage):
                    valid_combos.remove(combo)
        return valid_combos
    
    def find_shortest_light_solution(self) -> None:
        combos = self.find_valid_combos(self.light_sequence)
        self.shortest_light_solution = combos[0]

    def press_buttons_joltage(self, start_joltage: list[int], list_of_button_presses: list[str]) -> list[int]:
        current_joltage = start_joltage[:]
        press_calc = [0] * len(start_joltage)
        for button_press in list_of_button_presses:
            for i in range(0, len(press_calc)):
                if str(i) in button_press:
                    press_calc[i] += 1
        for i in range(0, len(press_calc)):
            current_joltage[i] -= press_calc[i]
        return current_joltage

    def make_joltage_light_sequence(self, current_joltage: list[int]) -> str:
        joltage_light_seq = ""
        for digit in current_joltage:
            if digit % 2 == 0:
                joltage_light_seq = joltage_light_seq + "."
            else:
                joltage_light_seq = joltage_light_seq + "#"
        return joltage_light_seq
    
    ###### JOLTAGE SOLUTION ##########
    def find_shortest_joltage_solution(self, current_joltage: list[int]) -> int:
        shortest_joltage_solution_so_far = 1000000000
        current_button_presses = 0
        #create light sequence from joltage
        joltage_light_seq = self.make_joltage_light_sequence(current_joltage)
        #create valid combos for final joltage sequence:
        valid_final_combos = self.find_valid_combos(joltage_light_seq, current_joltage)
        print("current joltage: ", current_joltage, " valid combos: ", valid_final_combos)
        #if there are no valid combos: -> return max button pressses. not valid
        if len(valid_final_combos) == 0:
            return shortest_joltage_solution_so_far
        for combo in valid_final_combos:
            iter_current_joltage = current_joltage[:]#joltage after button press
            combo_current_joltage = self.press_buttons_joltage(iter_current_joltage, combo)[:]
            print("current combo: ", combo, " after press:", combo_current_joltage)
            current_button_presses = len(combo)
            #was this press the end?
            if all(digit == 0 for digit in combo_current_joltage):
                #if it is the lowest amount of presses so far
                if current_button_presses < shortest_joltage_solution_so_far:
                    shortest_joltage_solution_so_far = current_button_presses
            # if anything goes negative, failure
            elif any(digit < 0 for digit in combo_current_joltage):
                current_button_presses = 1000000000
                print("combo failed")
            # all other cases - not all 9, and not negative values
            else:
                #step 1 complete - send to step 2, carrying back the button presses
                current_button_presses += self.solve_current_joltage_r(combo_current_joltage)
                if current_button_presses < shortest_joltage_solution_so_far:
                    shortest_joltage_solution_so_far = current_button_presses
        return shortest_joltage_solution_so_far
            
    def solve_current_joltage_r(self, current_joltage: list[int]) -> int:
        current_lowest_so_far = 1000000000
        print("current joltage: ", current_joltage)

        valid_moves_from_here = self.find_valid_combos(self.make_joltage_light_sequence(current_joltage))
        if len(valid_moves_from_here) > 0:
            current_presses = self.find_shortest_joltage_solution(current_joltage)
        if all(digit % 2 == 0 for digit in current_joltage): #if all are even:
            new_joltage = list(map(lambda d: d // 2, current_joltage))[:] #divide by 2
            print("all even! dividing by two: ", new_joltage)
            current_presses = 2 * self.solve_current_joltage_r(new_joltage) #2 * recursive
            if current_presses < current_lowest_so_far:
                current_lowest_so_far = current_presses
        if current_lowest_so_far == 1000000000: 
            print("no options from here")
        return current_lowest_so_far
        




def create_machine_from_string(machine:str) -> Machine:
    list_strings = machine.split(" ")
    light_sequence = list_strings[0].strip("[").strip("]")
    joltage = list_strings[-1]
    list_buttons = list_strings[1:-1]
    return Machine(light_sequence, list_buttons, joltage)

def create_machines_from_input(input: str) -> list[Machine]:
    list_str = input.split("\n")
    list_machines = []
    for str in list_str:
        list_machines.append(create_machine_from_string(str))
    return list_machines

def calc_total_shortest(list_machines: list[Machine], to_solve_for: str) -> int:
    total = 0
    for machine in list_machines:
        if to_solve_for == "light":
            total += len(machine.shortest_light_solution)
        if to_solve_for == "joltage":
            total += machine.shortest_joltage_solution
            print("index: ", list_machines.index(machine), "Solution: ",machine.shortest_joltage_solution)
    return total


def main():
    to_solve_for = ""
    if question_part == 1:
        to_solve_for = "light"
    if question_part == 2:
        to_solve_for = "joltage"
    list_of_machines = create_machines_from_input(puzzleinput)
    #list_of_machines = [create_machine_from_string("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}")]
    #print(list_of_machines[0].joltage_sequence)
    #print(list_of_machines[0].shortest_joltage_solution)
    result = calc_total_shortest(list_of_machines, to_solve_for)
    print("Answer: ", result)

if __name__ == "__main__":
    main()
