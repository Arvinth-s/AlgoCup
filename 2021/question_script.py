#OM NAMO NARAYANA
import numpy as np
import os

def new_case(name):
    name = str(name)
    question_file = open('./input/ifile{}.txt'.format(name), 'w')
    answer_file = open('./output/ofile{}.txt'.format(name), 'w')
    return [question_file, answer_file]


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
count = 0
n_max = int(1e5)
m_max = n_max-1

values = np.arange(1, 1+n_max)
edges = np.arange(0, m_max+1)
np.random.shuffle(edges)


'''
    Edge cases
    case 1: All in ascending order
    case 2: All in descending order
    case 3: First increasing and then decreasing
    case 4: First decreasing and then increasing
'''

qfile, afile = new_case(count)
qfile.write(str(n_max) + " " + str(m_max) + "\n")
for i in range(1, n_max+1):
    qfile.write(str(i) + " ")
qfile.write("\n")
for i in range(0, m_max):
    qfile.write(str(i) + " " + str(i+1)+"\n")
qfile.write('10000000')
