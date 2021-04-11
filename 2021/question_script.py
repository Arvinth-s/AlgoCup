#OM NAMO NARAYANA
import numpy as np
import os
import random


count = 0
n_max = int(1e1)
m_max = n_max-1

def new_case(name):
    name = str(name)
    question_file = open('./input/ifile{}.txt'.format(name), 'w')
    answer_file = open('./output/ofile{}.txt'.format(name), 'w')
    return [question_file, answer_file]


'''
    code from gfg
'''
def max_area_histogram(histogram):

    # This function calulates maximum 
    # rectangular area under given 
    # histogram with n bars
  
    # Create an empty stack. The stack 
    # holds indexes of histogram[] list. 
    # The bars stored in the stack are
    # always in increasing order of 
    # their heights.
    stack = list()
  
    max_area = 0 # Initialize max area
  
    # Run through all bars of
    # given histogram
    index = 0
    while index < len(histogram):
          
        # If this bar is higher 
        # than the bar on top
        # stack, push it to stack
  
        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1
  
        # If this bar is lower than top of stack,
        # then calculate area of rectangle with 
        # stack top as the smallest (or minimum
        # height) bar.'i' is 'right index' for 
        # the top and element before top in stack
        # is 'left index'
        else:
            # pop the top
            top_of_stack = stack.pop()
  
            # Calculate the area with 
            # histogram[top_of_stack] stack
            # as smallest bar
            area = (histogram[top_of_stack] * 
                   ((index - stack[-1] - 1) 
                   if stack else index))
  
            # update max area, if needed
            max_area = max(max_area, area)
  
    # Now pop the remaining bars from 
    # stack and calculate area with 
    # every popped bar as the smallest bar
    while stack:
          
        # pop the top
        top_of_stack = stack.pop()
  
        # Calculate the area with 
        # histogram[top_of_stack] 
        # stack as smallest bar
        area = (histogram[top_of_stack] * 
              ((index - stack[-1] - 1) 
                if stack else index))
  
        # update max area, if needed
        max_area = max(max_area, area)
  
    # Return maximum area under 
    # the given histogram
    return max_area


def convert_to_histogram(values, edges_list):
    res = 0
    for edges in edges_list:
        hist = values[:len(edges)]
        values = values[len(edges):]
        res = max(res, max_area_histogram(hist))
    return res


def add_case(values, edges_list):
    global count
    n = len(values)
    m = 0 
    for edges in edges_list:
        m += len(edges)-1
    qfile, afile = new_case(count)
    qfile.write('{} {}\n'.format(n, m))
    for value in values:
        qfile.write(str(value) + " ")
    qfile.write('\n')
    for edges in edges_list:
        for i in range(len(edges)-1):
            qfile.write('{} {}\n'.format(edges[i], edges[i+1]))
    qfile.write('\n')


    res = convert_to_histogram(values, edges_list)
    assert(res < int(1e9))
    sign = 2*np.random.randint(2)-1
    noise = np.random.randint(int(res/2))
    qfile.write(str(noise*sign+res))
    assert(sign==1 or sign==-1)
    if(sign < 0 or noise == 0):
        afile.write('Heaven')
    else:
        afile.write('Hell')
    qfile.close()
    afile.close()
    count += 1
    return res


    
    

'''
    If directory doesn't exist create one. If it exists os.mkdir returns error. Ignore it
'''
try:
    os.mkdir('./input')
except:
    '''do nothing'''
try:
    os.mkdir('./output')
except:
    '''do nothing'''

'''
    count is to name the file
    n_max is the maximum number of nodes and m_max is maximum number of paths
'''





'''
    Edge cases
    case 1: All in ascending order
    case 2: All in descending order
    case 3: First decreasing and then increasing
    case 4: First increasing and then decreasing
    case 5: No islands are connected
'''



'''case1: '''
n=n_max
values = list(np.arange(1, 1+n))
edges = [list(np.arange(len(values)))]
random.shuffle(edges[0])
res = add_case(values, edges)


'''case2: '''
n=n_max
values = list(np.arange(1, 1+n))
values.reverse()
edges = [list(np.arange(len(values)))]
random.shuffle(edges[0])
res = add_case(values, edges)


'''case3: '''
n=n_max
temp_values = list(np.arange(1, int((1+n)/2)))
values = temp_values.copy()
temp_values.reverse()
values = values + temp_values
edges = [list(np.arange(len(values)))]
random.shuffle(edges[0])
res = add_case(values, edges)

'''case4: '''
n=n_max
temp_values = list(np.arange(1, int((1+n)/2)))
values = temp_values.copy()
temp_values.reverse()
values = temp_values + values
edges = [list(np.arange(len(values)))]
random.shuffle(edges[0])
res = add_case(values, edges)


'''case 5:'''
n=n_max
values = list(np.arange(1, 1+n))
edges_temp = [list(np.arange(len(values)))]
random.shuffle(edges_temp[0])
edges = []
for edge in edges_temp[0]: 
    edges.append([edge])
res = add_case(values, edges)


'''random cases with n < n_max/2'''
num_cases = 5
for caseno in range(num_cases):
    n = max(5, np.random.randint(int(n_max/2)))
    values = list(np.arange(1, 1+n))
    random.shuffle(values)

    num_partitions = max(2, np.random.randint(n-1))

    edges_temp = [list(np.arange(len(values)))]
    random.shuffle(edges_temp[0])
    edges = []
    partitions = list(set(np.random.randint(n-1, size=num_partitions)))
    partitions.sort()

    '''debugging'''

    '''
    print('edges:', edges_temp)
    print('partitions:', partitions)
    '''

    num_partitions = len(partitions)
    for i in range(num_partitions-1): 
        edges = edges + [edges_temp[0][partitions[i] : partitions[i+1]]]
    edges = edges + [edges_temp[0][partitions[num_partitions-1] : ]]

    res = add_case(values, edges)
    print(res)

'''random cases with n > n_max/2'''
num_cases = 5
for caseno in range(num_cases):
    n = int(n_max/2) + max(5, np.random.randint(int(n_max/2)))
    values = list(np.arange(1, 1+n))
    random.shuffle(values)

    num_partitions = max(2, np.random.randint(n-1))

    edges_temp = [list(np.arange(len(values)))]
    random.shuffle(edges_temp[0])
    edges = []
    partitions = list(set(np.random.randint(n-1, size=num_partitions)))
    partitions.sort()

    '''debugging'''

    '''
    print('edges:', edges_temp)
    print('partitions:', partitions)
    '''

    num_partitions = len(partitions)
    for i in range(num_partitions-1): 
        edges = edges + [edges_temp[0][partitions[i] : partitions[i+1]]]
    edges = edges + [edges_temp[0][partitions[num_partitions-1] : ]]

    res = add_case(values, edges)
    print(res)