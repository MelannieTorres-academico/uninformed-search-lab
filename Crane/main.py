#Alan Kuri & Melannie Torres

import sys
from itertools import *
from pprint import pprint
from collections import OrderedDict
from copy import deepcopy

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
'''
# Consistent Heuristic, every different letter in different order is 1+
def heuristic_consistent(max_height, actual_state, goal_state):
    print()
    for i in range(max_height):
        print('ACTUAL', actual_state[i], 'GOAL', goal_state[i])
        alan_putito = set(actual_state[i]).intersection(set(goal_state[i]))
        print(alan_putito)
    pass
'''
def heuristic_consistent(max_height, actual_state, goal_state):
    lel = 0
    for i, h in zip(actual_state, goal_state):
        for e, k in zip_longest(i, h):
            if e != k:
                lel = lel + 1
    return lel


def calculateCostOfMoveBox(i, j):
    actionCost = 1 + (abs(i - j))
    
    return actionCost
    
def moveBox(original_current_node, i, j):
    current_node = deepcopy(original_current_node)
    node = {}
    #remove node from column i
    for element in current_node['state'][i]:
        if element != []:
            node = element
            current_node['state'][i].remove(element)
            #put node in j
            current_node['state'][j].append(node)
            break
    return current_node

def actions(current_node, max_height, frontier, goal):
    num_cols = len(current_node)
    
    tot = current_node['state']

    #remove repeted states
    for i in range(num_cols):
        for j in range(num_cols):
            if (i != j):
                if (len(tot[j]) < max_height): #checks if stack is full7
                    if (len(tot[i]) != 0): #checks that the place where we'll remove the box is not empty
                        cost = calculateCostOfMoveBox(i, j)
                        tut = moveBox(current_node, i, j)
    return tut
    
    

def goal_test(actual_state, goal_state):
    print()
    if(actual_state == goal_state):
        return True
    return False
    
#https://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
#h=0
def treeSearch (max_height, start, goal):
    frontier = Q.PriorityQueue()
    nodes = {
        'state': start,
        'total_cost': 0
    }
    visited = []
    
    frontier.put((0, nodes))
    
    i = 0
    while i <= 5:
        if frontier.empty():
            print('NO HAY NADA EN FRONTIER')
            return False
        print('POP FROM QUEUE', frontier.queue)
        print('current_node', frontier.queue[0])
        current_node = frontier.queue[0]  #problema, no sabe por qué ordenar la priority queue
        
        
        if goal_test(current_node['state'], goal):
            print('SOLUTION FOUND')
            break
        
        visited.append(current_node)
        new_node = actions(current_node, max_height, frontier, goal)
        print('NEW NODE', new_node)
        print('V:', visited)
        print('F:', frontier.queue)
        

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

print("-----Heuristic_consistent------")
#heuristic_consistent(max_height, cont_start, cont_goal)

print("----Actions-----")
#frontier = Q.PriorityQueue()

#print(cont_start)
#actions(cont_start, 3, frontier)

treeSearch (max_height, cont_start, cont_goal)
        
    