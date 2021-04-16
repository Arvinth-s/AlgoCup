#OM NAMO NARAYANA
import numpy as np
import os
import random


count = 0
n_max = int(1e5)
val_max = int(1e4)
mode = "judgement_day"
# mode = "uploaded"

'''
    count is to name the file
    n_max is the maximum number of nodes 


'''

def new_case(name):
    name = str(name)
    question_file = open('./' + mode + '/input/input{}.txt'.format(name), 'w')
    answer_file = open('./' + mode + '/output/output{}.txt'.format(name), 'w')
    log_file = open('./' + mode + '/log/log{}.txt'.format(name), 'w')
    return [question_file, answer_file, log_file]


'''
    code from gfg
'''
def max_area_histogram(histogram, log_file):

    # log_file.write(str(histogram)+'\n')
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


def convert_to_histogram(values, edges_list, log_file):
    res = 0
    for edges in edges_list:
        hist = [values[i] for i in edges]
        # values = values[len(edges):]
        buffer = max_area_histogram(hist, log_file)
        if(buffer > res):
            res = buffer
        # print(values)
            # log_file.truncate(0)
            # for i in hist:
                # log_file.write(str(i) + " ")
    return res


def add_case(values, edges_list):
    global count
    n = len(values)
    m = 0 
    values = [min(val_max, value) for value in values]
    for edges in edges_list:
        m += len(edges)-1
    qfile, afile, log_file = new_case(count)
    # log_file.write(str(edges_list) + '\n')
    qfile.write('{} {}\n'.format(n, m))
    for value in values:
        qfile.write(str(value) + " ")
    qfile.write('\n')
    for edges in edges_list:
        for i in range(len(edges)-1):
            qfile.write('{} {}\n'.format(edges[i], edges[i+1]))
    qfile.write('\n')


    res = convert_to_histogram(values, edges_list, log_file)
    assert(res < int(1e9))
    # sign = 2*np.random.randint(2)-1
    # noise = min(int(1e9)-res,  np.random.randint(int(res/2)))
    # qfile.write(str(noise*sign+res))
    # assert(sign==1 or sign==-1)

    '''
    if(sign < 0 or noise == 0):
        afile.write('Heaven')
    else:
        afile.write('Hell')
    '''

    #for debugging
    afile.write(str(res))


    qfile.close()
    afile.close()
    log_file.close()
    count += 1

    if(res == max(values)):
        print('res is maximum of values')

    return res


    

'''
    If directory doesn't exist create one. If it exists os.mkdir returns error. Ignore it
'''
try:
    os.mkdir('./'+mode)
except:
    '''do nothing'''

try:
    os.mkdir('./' + mode +  '/input')
except:
    '''do nothing'''
try:
    os.mkdir('./'+ mode +'/output')
except:
    '''do nothing'''
try:
    os.mkdir('./'+ mode +'/log')
except:
    '''do nothing'''

'''





Driver code



'''



'''sample cases'''

'''sample case 1:'''
values = [1, 5, 3, 9, 4]
edges = [[0, 1, 2], [3, 4]]
res = add_case(values, edges)


'''sample case 2:'''
values = [1, 6, 2, 3, 8]
edges = [[0], [1, 2], [3, 4]]
res = add_case(values, edges)


'''random cases with 5 < n < 10 for debugging'''
num_cases = 5
for caseno in range(num_cases):
    n = 5 + np.random.randint(5)
    values = list(np.arange(1, 1+n))
    random.shuffle(values)

    num_partitions = max(2, np.random.randint(n-1))

    edges_temp = [list(np.arange(len(values)))]
    random.shuffle(edges_temp[0])
    partitions = list(set(np.random.randint(n-1, size=num_partitions)))
    partitions.sort()
    edges = []

    if(partitions[0] > 0):
        edges = [edges_temp[0][:partitions[0]]]

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