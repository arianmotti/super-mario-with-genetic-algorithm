import random
import math


class Combined:
    def __init__(self, allgenes, goodgenes, goodpoints):
        self.allgenes = allgenes
        self.goodgenes = goodgenes
        self.combinedlist = []
        self.goodpoints = goodpoints
        self.better = zip(self.goodgenes, self.goodpoints)

    def combine(self):
        for i in range(len(self.goodgenes)):
            parent1 = self.goodgenes[random.randint(0, len(self.goodgenes) - 1)]
            parent2 = self.goodgenes[random.randint(0, len(self.goodgenes) - 1)]
            self.crossover(parent1, parent2)
            self.combinedlist.append(self.crossover(parent1, parent2))
            # parent1 = self.goodgenes[random.randint(0, len(self.goodgenes) - 1)]
            # parent2 = self.goodgenes[random.randint(0, len(self.goodgenes) - 1)]
            # self.crossover(parent1, parent2)
            # self.combinedlist.append(self.crossover(parent1, parent2))
        return self.combinedlist

    def crossover(self, p1, p2):
        child1 = []
        child2 = []
        for i in range(math.floor(len(p1) / 2)):
            child1.append(p1[i])

        for j in range(math.floor(len(p1) / 2), len(p1)):
            child1.append(p2[j])

        for i in range(math.floor(len(p1) / 2)):
            child2.append(p2[i])
        for j in range(math.floor(len(p1) / 2), len(p1)):
            child2.append(p1[j])

        return child1, child2


# addition
class FirstPop:
    def __init__(self, level):
        self.first_pop_list = []
        self.first_pop_state = []

        self.lenght = len(level)

    def build(self):
        for i in range(self.lenght):
            self.first_pop_list.append(random.randint(0, 2))
        # print(self.first_pop_list)
        return self.first_pop_list

    def state_maker(self):
        state = 's0'
        self.first_pop_state.append(state)
        for i in range(self.lenght - 1):

            if state == 's0':
                if self.first_pop_list[i + 1] == 0:
                    state = 's0'
                if self.first_pop_list[i + 1] == 1:
                    state = 's1'
                if self.first_pop_list[i + 1] == 2:
                    state = 's2'

            elif state == 's1':
                if self.first_pop_list[i + 1] == 0:
                    state = 's0'
                if self.first_pop_list[i + 1] == 1:
                    state = 's0'
                if self.first_pop_list[i + 1] == 2:
                    state = 's0'
            elif state == 's2':
                if self.first_pop_list[i + 1] == 0:
                    state = 's0'
                if self.first_pop_list[i + 1] == 1:
                    state = 's1'
                if self.first_pop_list[i + 1] == 2:
                    state = 's2'
            self.first_pop_state.append(state)
        return self.first_pop_state


class Game:

    def __init__(self, levels):
        # Get a list of strings as levels
        # Store level length to determine if a sequence of action passes all the steps

        self.levels = levels
        self.current_level_index = -1
        self.current_level_len = 0

        # addition
        # self.first_pop_list = []
        # self.first_pop_statelist = []

    def load_next_level(self):
        self.current_level_index += 1
        self.current_level_len = len(self.levels[self.current_level_index])

    def get_score(self, states):
        # Get an action sequence and determine the steps taken/score
        # Return a tuple, the first one indicates if these actions result in victory
        # and the second one shows the steps taken
        point = 0

        current_level = self.levels[self.current_level_index]
        steps = 0
        for i in range(self.current_level_len - 1):
            current_step = current_level[i]
            if current_step == '_':
                steps += 1
            elif current_step == 'G' and states[i] == 's1':
                steps += 1
            elif current_step == 'L' and states[i] == 's2':
                steps += 1
            if current_step == 'M' and states[i] != 's1':
                point = point + 2
            if i == self.current_level_len - 1 and states[i] == 's1':
                point = point + 2
            if (current_step == '_' or current_step == 'G') and states[i] == 's1' and current_step != 'M' and \
                    current_level[i + 1] == 'G':
                point = point + 2
            if current_step == '_' and current_level[i + 1] == '_' and states[i] == 's1':
                point = point - 0.5

            #
            # else:
            #     break
        if steps == self.current_level_len - 1:
            point = point + 10
        else:
            point = point - 5

        print(steps == self.current_level_len - 1, steps)
        return point


# class Selection:
#     def __init__(self):
print('enter your level :')
level = input()

g = Game([level])
g.load_next_level()

print('enter your first population amount :')
amount = int(input())
# addition
states = []
points = []
points2 = []
total_points = 0
for i in range(amount):
    test = FirstPop(level)
    print(test.build())
    states.append(test.state_maker())
    print(states[i])
    points.append(g.get_score(test.state_maker()))
    print(points[i])
# total_points = total_points + points[i]
for j in range(len(points)):
    points2.append(abs(points[j]))
selection = zip(points, states)
selection2 = zip(points2, states)

selection = tuple(selection)
selection = sorted(selection)
#print(selection)
selection2 = tuple(selection2)
selection2 = sorted(selection2)
randomList = random.choices(states, weights=points2, k=math.floor(len(points) / 2))
goodpoints = []
for i in range((len(randomList))):
    goodpoints.append(g.get_score(randomList[i]))

#print(randomList)
combined = Combined(selection, randomList, goodpoints)
combined_list = combined.combine()
print(combined_list)

# print(len(randomList), len(goodpoints))

# This outputs (False, 4)
# print(g.get_score("0000000000"))
