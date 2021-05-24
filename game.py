import random
import enum


class States(enum.Enum):
    state1 = 1
    state2 = 2
    sttate3 = 3


class FirstPop:
    def __init__(self, level):
        self.first_pop_list = []
        self.first_pop_statelist = []
        for i in range(len(level)):
            self.first_pop_list.append(random.randint(0, 2))
        print(self.first_pop_list)
        self.first_pop_statelist.append(States.state1)
        print(self.first_pop_statelist)
        for i in range(0, len(level) - 1):
            if self.first_pop_statelist[i] == States.state1:
                if self.first_pop_list[i] == 0:
                    self.first_pop_statelist.append(States.state1)
                if self.first_pop_list[i] == 1:
                    self.first_pop_statelist.append(States.state2)
                if self.first_pop_list[i] == 2:
                    self.first_pop_statelist.append(States.state3)

                if self.first_pop_statelist[i] == States.state2:
                    self.first_pop_statelist.append(States.state1)
                if self.first_pop_statelist[i] == States.state3:
                    if self.first_pop_list[i] == 0:
                        self.first_pop_statelist.append(States.state1)
                    if self.first_pop_list[i] == 1:
                        self.first_pop_statelist.append(States.state2)
                    if self.first_pop_list[i] == 2:
                        self.first_pop_statelist.append(States.state3)


class Game:

    def __init__(self, levels):
        # Get a list of strings as levels
        # Store level length to determine if a sequence of action passes all the steps

        self.levels = levels
        self.current_level_index = -1
        self.current_level_len = 0

        # addition
        self.first_pop_list = []
        self.first_pop_statelist = []

    def load_next_level(self):
        self.current_level_index += 1
        self.current_level_len = len(self.levels[self.current_level_index])

    def get_score(self, actions):
        # Get an action sequence and determine the steps taken/score
        # Return a tuple, the first one indicates if these actions result in victory
        # and the second one shows the steps taken

        current_level = self.levels[self.current_level_index]
        steps = 0
        for i in range(self.current_level_len - 1):
            current_step = current_level[i]
            if current_step == '_':
                steps += 1
            elif current_step == 'G' and actions[i - 1] == '1':
                steps += 1
            elif current_step == 'L' and actions[i - 1] == '2':
                steps += 1
            else:
                break
        return steps == self.current_level_len - 1, steps


g = Game(["____G__L__", "___G_M___L_"])
g.load_next_level()
test = FirstPop('0000000000')

# This outputs (False, 4)
print(g.get_score("0000000000"))
