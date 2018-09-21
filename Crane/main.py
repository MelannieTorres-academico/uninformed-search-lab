#Alan Kuri A01204805 & Melannie Torres A01361808

import sys
from itertools import *
from collections import OrderedDict
from copy import deepcopy

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

def heuristic_consistent(max_height, actual_state, goal_state):
    lel = 0
    for i, h in zip(actual_state, goal_state):
        for e, k in zip_longest(i, h):
            if e != k:
                lel = lel + 1

    return 0

def calculateCostOfMoveBox(i, j):
    actionCost = 1 + (abs(i - j))

    return actionCost

def moveBox(original_current_node, i, j):
    current_node = deepcopy(original_current_node)
    node = {}
    #remove node from column i
    for element in current_node[i]:
        if element != []:
            node = element
            current_node[i].remove(element)
            current_node[j].append(node)
            break
    return current_node

def actions(current_node, max_height, frontier, goal, visited, last_cost, path):
    #check for all possible states
    num_cols = len(current_node)
    tot = current_node

    for i in range(num_cols):
        for j in range(num_cols):
            if (i != j):
                if (len(tot[j]) < max_height): #checks if stack is full7
                    if (len(tot[i]) != 0): #checks that the place where we'll remove the box is not empty
                        new_cost = last_cost
                        new_cost += calculateCostOfMoveBox(i, j)
                        tut = moveBox(current_node, i, j)
                        priority = new_cost + heuristic_consistent(max_height, current_node, goal)
                        c = None
                        if not frontier.empty():
                           p, c, n, a = frontier.queue[0]

                        if tut not in visited and tut not in frontier.queue:
                            frontier.put((priority, new_cost, moveBox(current_node, i, j), path[:] + [(i, j)] ))
                        elif c is not None and c > new_cost:
                            frontier.get()
                            frontier.put((priority, new_cost, moveBox(current_node, i, j), path[:]  + [(i, j)] ))


def goal_test(actual_state, goal_state, cost, action):

    if(actual_state == goal_state):
        return True

    for ac, go in zip(actual_state, goal_state):
        for a, g in zip_longest(ac, go):
            if(g == 'X'):
                continue
            if(g != a):
                return False

    return True

#https://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
#h=0
def treeSearch (max_height, start, goal):
    frontier = Q.PriorityQueue()
    visited = []

    frontier.put((0, 0, start, []))

    while True:
        if frontier.empty():
            print('No solution found')
            return False

        priority, cost, current_node, path = frontier.get()

        if goal_test(current_node, goal, cost, path):
            print(cost)
            print(str(path).replace("[", "").replace("]", "").replace("),", ");"))
            return True

        visited.append(current_node)
        actions(current_node, max_height, frontier, goal, visited, cost, path)



#Read all lines in txt
data = sys.stdin.readlines()

# Get variables from array
max_height = int(data[0].rstrip('\n'))
start = data[1].rstrip('\n')
goal = data[2].rstrip('\n')

#Replace and Split of start string
cont_start = []
for element in start.split(";"):
    parse_start = list(filter(None, element.replace('(', "").replace(')', "").replace(' ', "").split(',')))
    cont_start.append(parse_start)


#Replace and Split of goal string
cont_goal = []
for element in goal.split(";"):
    parse_goal = list(filter(None, element.replace('(', "").replace(')', "").replace(' ', "").split(',')))
    cont_goal.append(parse_goal)

#Execute
treeSearch (max_height, cont_start, cont_goal)
