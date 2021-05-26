import random
import math
import matplotlib.pyplot as plt


def draw_vertical_columnbar_line_with_stem_method(array):
    # The x-axis maximum number.
    axis_x_max = 10

    axis_y_max = 20

    y_value = array

    x_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    plt.xlim(0, axis_x_max)

    plt.ylim(-axis_y_max, axis_y_max)

    plt.stem(x_value, y_value)

    plt.show()


class Combined:
    def __init__(self, allgenes, goodgenes, goodpoints, g, countwinscore):
        self.allgenes = allgenes
        self.goodgenes = goodgenes
        self.combinedlist = []
        self.goodpoints = goodpoints
        self.newpoints = []
        self.better = zip(self.goodgenes, self.goodpoints)
        self.game = g
        self.countwinscore = countwinscore

    def combine(self):
        # print(self.goodgenes)
        for i in range(len(self.goodgenes)):
            parent1 = self.goodgenes[random.randint(0, len(self.goodgenes) - 1)]
            parent2 = self.goodgenes[random.randint(0, len(self.goodgenes) - 1)]
            child1, child2 = self.crossover(parent1, parent2)
            # print(parent1)
            # print(parent2)
            # print(child1)
            # print(child2)
            self.combinedlist.append(child1)
            self.combinedlist.append(child2)
            # parent1 = self.goodgenes[random.randint(0, len(self.goodgenes) - 1)]
            # parent2 = self.goodgenes[random.randint(0, len(self.goodgenes) - 1)]
            # self.crossover(parent1, parent2)
            # self.combinedlist.append(self.crossover(parent1, parent2))
            self.newpoints.append(g.get_score(child1, self.countwinscore))
            self.newpoints.append(g.get_score(child2, self.countwinscore))
        return self.combinedlist

    def newpoints(self):
        return self.newpoints

    def totalnewpoints(self):
        total = 0
        for i in range(len(self.newpoints)):
            total = total + self.newpoints[i]
        return total

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
        child1 = self.mutation(child1)
        child2 = self.mutation(child2)

        return child1, child2

    def mutation(self, child):
        x = random.random()
        if x >= 0.1:
            child[random.randint(0, len(child) - 1)] = 's0'
        return child


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
        self.success = False

        # addition
        # self.first_pop_list = []
        # self.first_pop_statelist = []

    def load_next_level(self):
        self.current_level_index += 1
        self.current_level_len = len(self.levels[self.current_level_index])

    def get_score(self, states, countwinscore):
        # Get an action sequence and determine the steps taken/score
        # Return a tuple, the first one indicates if these actions result in victory
        # and the second one shows the steps taken
        point = 0

        current_level = self.levels[self.current_level_index]
        steps = 0
        for i in range(self.current_level_len - 1):
            current_step = current_level[i]
            if current_step == '_' or current_step == 'M':
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
            if countwinscore:
                point = point + 10
            self.success = True


        else:
            if countwinscore:
                point = point - 5
            self.success = False

        # print(steps == self.current_level_len - 1, steps)
        return point

    def success(self):
        return self.success


print('enter your level :')
level = input()

g = Game([level])
g.load_next_level()

print('enter your first population amount :')
amount = int(input())

print('count win score?\n press y to yes and press n to no ')
countwinscore = input()
if countwinscore == 'y':
    countwinscore = True
print('choose your method for selection : \n press 1 or 2')
method = input()

# addition
states = []
points = []
points2 = []
total_points = 0
all_total_points = []
max_point = 0
min_point = 0
all_maxpoints = []
all_minpoints = []
win = 0
for i in range(amount):
    test = FirstPop(level)
    print(test.build())
    states.append(test.state_maker())
    print(states[i])
    points.append(g.get_score(states[i], countwinscore))
    if g.success:
        win = 1
        print('we reached goal in the first step')

    # print(points[i])
    total_points = total_points + points[i]

success = False

min_point = min(points)
max_point = max(points)
all_maxpoints.append(max_point)
all_minpoints.append(min_point)

all_total_points.append(total_points)
# print(total_points)
for j in range(len(points)):
    points2.append(abs(points[j]))
selection = zip(points, states)
selection2 = zip(points2, states)

selection = tuple(selection)
selection = sorted(selection)

# print(selection)
selection2 = tuple(selection2)
selection2 = sorted(selection2)
# print(states)
# print(len(states), len(points2))
algo_repeat: int = 10
for algo in range(algo_repeat - 1):

    if method == '1':
        randomList = random.choices(states, weights=points2, k=math.floor(len(states) / 2))
    else:
        states = [states for points2, x in selection2]
        randomList = []

        for i in range(math.floor(len(states) / 2)):
            randomList.append(states[i])

    # print(randomList)
    # randomList = randomList[:len(randomList)-(len(randomList)//2)]
    # print(randomList)
    goodpoints = []
    tmp_points = 0
    for i in range((len(randomList))):
        goodpoints.append(g.get_score(randomList[i], countwinscore))
    # print(goodpoints)

    combined = Combined(selection, randomList, goodpoints, g, countwinscore)
    combined_list = combined.combine()
    # print(combined_list)
    states = combined_list
    for i in range(len(states)):
        g.get_score(states[i], countwinscore)
        if g.success:
            win = algo + 2
            print(f'we reached goal in the {algo} step')
            break

        # print(points[i])
        total_points = total_points + points[i]

    points2 = []
    all_maxpoints.append(max(combined.newpoints))
    all_minpoints.append(min(combined.newpoints))
    for j in range(len(points)):
        points2.append(abs(combined.newpoints[j]))
    for j in range(len(points2)):
        tmp_points = tmp_points + points2[j]
    all_total_points.append(tmp_points)
    # print(combined.totalnewpoints())
    # print(len(states), len(points2), 'here')
# print(all_total_points)
avg_total_points = []
for i in range(len(all_total_points)):
    avg_total_points.append(all_total_points[i] / amount)
# print(avg_total_points)

draw_vertical_columnbar_line_with_stem_method(avg_total_points)
draw_vertical_columnbar_line_with_stem_method(all_maxpoints)
draw_vertical_columnbar_line_with_stem_method(all_minpoints)
# print(combined_list[0])

# print(len(randomList), len(goodpoints))

# This outputs (False, 4)
# print(g.get_score("0000000000"))
