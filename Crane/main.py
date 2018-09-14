import sys
from pprint import pprint

#Read all lines in txt
data = sys.stdin.readlines()

# Get variables from array
max_height = data[0].replace('\n', '')
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
