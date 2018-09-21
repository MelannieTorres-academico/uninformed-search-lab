#Alan Kuri A01204805 & Melannie Torres A01361808

import sys
from itertools import *
from pprint import pprint
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
    #print('CALCULATE COST')
    actionCost = 1 + (abs(i - j))

    return actionCost

def moveBox(original_current_node, i, j):
    #print('MOVE BOX')
    current_node = deepcopy(original_current_node)
    node = {}
    #remove node from column i
    for element in current_node[i]:
        #print('ELEMENT', element)
        if element != []:
            node = element
            current_node[i].remove(element)
            #put node in j
            current_node[j].append(node)
            break
    #print('return move box', current_node)
    return current_node

def actions(current_node, max_height, frontier, goal, visited):
    #check for all possible states
    #pprint('ACTIONS')
    num_cols = len(current_node)
    #print('CURRENT NODE', current_node)

    tot = current_node

    #remove repeted states

    for i in range(num_cols):
        for j in range(num_cols):
            if (i != j):
                #print('i', i, '!=', 'j', j)
                if (len(tot[j]) < max_height): #checks if stack is full7
                    #print(len(tot[j]), '<' ,max_height)
                    if (len(tot[i]) != 0): #checks that the place where we'll remove the box is not empty
                        #print(len(tot[i]), '!=', 0)
                        cost = calculateCostOfMoveBox(i, j)
                        #print('cost', cost)
                        # calculate h
                        #print('CALL TO MOVE BOX')
                        #print(moveBox(current_node, i, j))
                        tut = moveBox(current_node, i, j)
                        new_cost = cost + heuristic_consistent(max_height, current_node, goal)
                        #print(frontier.queue)
                        c = None
                        if not frontier.empty():
                            c, n, a = frontier.queue[0]

                        if tut not in visited and tut not in frontier.queue:
                            frontier.put((new_cost, moveBox(current_node, i, j), (i, j)))
                            #print(i, j)
                        elif c is not None and c > new_cost:
                            frontier.get()
                            frontier.put((new_cost, moveBox(current_node, i, j), (i, j)))
                            #print(i, j)
                        #print(i, j)

def goal_test(actual_state, goal_state, cost, action):
    #print(" GOAL STATE")
    #print("actual_state", actual_state)
    #print("goal_state", goal_state)
    lis = []
    if(actual_state == goal_state):
        #print("actual state es == goal_state")
        lis.append((actual_state, cost, action))
        #print("append el actual state cost y action a lista")
        print(actual_state, cost, action)
        return True

    for ac, go in zip(actual_state, goal_state):
        for a, g in zip_longest(ac, go):
            if(g == 'X'):
                #print('encontre x')
                continue
            if(g != a):
                return False
    lis.append((actual_state, cost, action))
   # print('LIS', lis)
    return True

#https://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
#h=0
def treeSearch (max_height, start, goal):
    frontier = Q.PriorityQueue()
    visited = []

    frontier.put((0, start, (0,0)))

    #i = 0
    while True:
        if frontier.empty():
            print('No solution found')
            return False

        cost, current_node, action = frontier.get()

        #print('current_node', current_node)
        if goal_test(current_node, goal, action, cost):
            #print('SOLUTION FOUND')
            print(cost)
            print(action)
            return True

        visited.append(current_node)
        actions(current_node, max_height, frontier, goal, visited)
        #print('V:', visited)
        #print('F:', frontier.queue)
        #poss_actions=actions(cont_start, max_height, frontier)
        #for action in poss_actions:
        #if action:
        #print("in for")
        #i += 1


        #print(new_node in visited)
        #print(new_node in frontier.queue)
        #new_cost = new_cost + heuristic_consistent(max_height, new_node, goal)
        #frontier.put((new_cost, new_node))


#Read all lines in txt
data = sys.stdin.readlines()

# Get variables from array
max_height = int(data[0].rstrip('\n'))
start = data[1].rstrip('\n')
goal = data[2].rstrip('\n')

#Replace and Split of start string
#print("\n######### Start String ###########")
cont_start = []
for element in start.split(";"):
    parse_start = list(filter(None, element.replace('(', "").replace(')', "").replace(' ', "").split(',')))
    cont_start.append(parse_start)
#print(parse_start)


#Replace and Split of goal string
#print("\n######### Goal String ###########")
cont_goal = []
for element in goal.split(";"):
    parse_goal = list(filter(None, element.replace('(', "").replace(')', "").replace(' ', "").split(',')))
    cont_goal.append(parse_goal)
    #print(parse_goal)


#print("\n######### Containers ###########")
#print(cont_start)
#print (cont_goal)
#print("-----Tree Search-----")
#treeSearch (max_height, cont_start, cont_goal)

#print("-----Heuristic_consistent------")
#heuristic_consistent(max_height, cont_start, cont_goal)

#print("----Actions-----")
#frontier = Q.PriorityQueue()

#print(cont_start)
#actions(cont_start, 3, frontier)

treeSearch (max_height, cont_start, cont_goal)


    
