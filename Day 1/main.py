from input import puzzleinput
#from testinput import puzzleinput

question_part = 2

class Dial():
    def __init__(self, question_part: int) -> None:
        self.marker = 50
        self.min = 0
        self.max = 99
        self.zero_count = 0
        self.question_part = question_part

    def __repr__(self) -> str:
        return (f"{self.marker}, {self.min}, {self.max}, {self.zero_count}")
    
    def turn_right(self, turns: int) -> None:
        for i in range(turns):
            self.marker += 1 
            if self.marker > self.max:
                self.marker = self.min
            if self.question_part == 2 and self.marker == 0:
                self.zero_count += 1
        
    def turn_left(self, turns: int) -> None:
        for i in range(turns):
            self.marker -= 1 
            if self.marker < self.min:
                self.marker = self.max
            if self.question_part == 2 and self.marker == 0:
                self.zero_count += 1

    def turn(self, turns: str) -> None:
        direction = turns[:1]  
        number = int(turns[1:])
        if direction == "R":
            self.turn_right(number)
        if direction == "L":
            self.turn_left(number)
        if self.question_part == 1 and self.marker == 0:
            self.zero_count += 1
        
def solve_turns(dial: Dial, str_of_turns: str) -> int:
    list_of_turns = list(str_of_turns.strip().split("\n"))
    for turn in list_of_turns:
        dial.turn(turn)
    return dial.zero_count



dial = Dial(question_part)
print("Answer: ",solve_turns(dial, puzzleinput))
