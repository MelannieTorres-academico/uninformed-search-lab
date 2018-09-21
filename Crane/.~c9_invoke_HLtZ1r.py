#Alan Kuri & Melannie Torres

import sys
from itertools import *
from pprint import pprint
from collections import OrderedDict

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
                print(e, k, lel)
    # LA QUE CUENTA ES LEL
    pass

def calculateCostOfMoveBox(current_node, i, j):
    actionCost = 1 + (abs(i - j))
    return actionCost
    
def moveBox(current_node, i, j):
    print(current_node)
    node=''
    #remove node from i
    for element in current_node[i]:
        print('a')
        if element != '':
            node=element
            element.replace(element, '')
            break
    #put node in j
    if node != '':
        for l, element in enumerate(current_node[j]):
            print('b')
            if element != '':
                current_node[j][l-1].replace(current_node[j][l-1], node)
                break        
    return current_node

def actions(current_node, max_height, fronti):
    #check for all possible states
    num_cols=len(current_node)
    
    #remove repeted states
    
    #
    """
    for a in range(current_node['states']):
        print(a)
    """
    for i in range(num_cols):
        for j in range(num_cols):
            if i != j:
                if len(current_node[j])<max_height: #checks if stack is full7
                    cost=calculateCostOfMoveBox(current_node, i, j)
                    # calculate h 
                    frontier.put(cost+h,moveBox(current_node, i, j))
    return frontier
    
    pass

def goal_test(actual_state, goal_state):
    print()
    if(actual_state == goal_state):
        return True
    return False
    
#https://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
h = 0

def treeSearch (max_height, start, goal):
    frontier = Q.PriorityQueue()
    nodes = {
        'state': start,
        'total_cost': 0,
        'path': []
    }
    visited = []
    
    frontier.put((0 + h, nodes))
    pprint(frontier.get()[1])
    while True:
        if frontier.empty():
            return False
        cost, current_node = frontier.get()
        
        if goal_test(current_node['state'], goal):
            print('SOLUTION FOUND')
            return
        
        visited.append(current_node)
        print('V:', visited)
'''       
        for action in actions:
            new_node = actions(current_node, max_height)
            if new_node not in visited or new_node not in frontier:
                new_node['total_cost'] = new_node['total_cost'] + heuristic_consistent(max_height, new_node, goal_test)
                frontier.put(new_node)
            elif new_node in frontier and frontier.get[1]['total_cost'] > new_node['total_cost']:
                new_node['total_cost'] = new_node['total_cost'] + heuristic_consistent(max_height, new_node, goal_test)
                frontier.put(new_node)
    
    pprint(visited)
'''

'''    
        if not frontier:
            print("The frontier is empty")
            return 0
        aux_current_node=frontier.get()
        if not aux_current_node:
            print("The frontier is empty")
            return 0
        print(aux_current_node)
        current_node=aux_current_node[1]

        if current_node == goal :#verify im removing the node
            print("Found goal output solution and continue")
        #expand all solutions and add them to the priority queue
        frontier=applyAllActions(current_node, len(current_node), max_height, frontier)
        print(current_node)    
        pass
'''

#Read all lines in txt
data = sys.stdin.readlines()

# Get variables from array
max_height = int(data[0].replace('\n', ''))
start = data[1].replace('\n', '')
goal = data[2].replace('\n', '')

#Replace and Split of start string
print("\n######### Start String ###########")
cont_start = []
for element in start.split(";"):
    parse_start = element.replace('(', '').replace(')', '').replace(' ', '').split(',')
    cont_start.append(parse_start)
    print(parse_start)
    
#Replace and Split of goal string
print("\n######### Goal String ###########")
cont_goal = []
for element in goal.split(";"):
    parse_goal = element.replace('(', '').replace(')', '').replace(' ', '').split(',')
    cont_goal.append(parse_goal)
    print(parse_goal)


print("\n######### Containers ###########")
print(cont_start)
print (cont_goal)
print("-----Tree Search-----")
#treeSearch (max_height, cont_start, cont_goal)

print("-----Heuristic_consistent------")
#heuristic_consistent(max_height, cont_start, cont_goal)

print("----Actions-----")
frontier = Q.PriorityQueue()

print(start)
moveBox(current_node, i, j)
#print(actions(start, max_height, frontier))

        
    