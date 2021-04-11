#OM NAMO NARAYANA
import numpy as np 
import random

for i in range(0, 10):
    ifile = open('.\ifile'+str(i)+'.txt', 'w')
    ofile = open('.\ofile'+str(i)+'.txt', 'w')
    T = np.random.randint(1, 10)
    ifile.write(str(T)+'\n')
    for t in range(T):
        N = np.random.randint(1, 100)
        ifile.write(str(N)+'\t')
        X = np.random.randint(0, N)
        ifile.write(str(X)+'\n')
        K = np.random.randint(2*X, 2*N)
        L = random.sample(range(2*N), K)
        st = list('M'*(2*N))
        for i in L:
            st[i] = 'F'
        s = ''
        for i in st:
            s += i
        ifile.write(s+'\n')
        if(K%3 == 0):
            ofile.write(str('YES') + '\n')
    ifile.close()
    ofile.close()
for i in range(10, 30):
    ifile = open('.\ifile'+str(i)+'.txt', 'w')
    ofile = open('.\ofile'+str(i)+'.txt', 'w')
    T = np.random.randint(1, 1000)
    ifile.write(str(T)+'\n')
    for t in range(T):
        N = np.random.randint(1, 100)
        ifile.write(str(N)+'\t')
        X = np.random.randint(0, N)
        ifile.write(str(X)+'\n')
        K = np.random.randint(2*X, 2*N)
        L = random.sample(range(2*N), K)
        st = list('M'*(2*N))
        for i in L:
            st[i] = 'F'
        s = ''
        for i in st:
            s += i
        ifile.write(s+'\n')
        if(K%3 == 0):
            ofile.write(str('YES') + '\n')
    ifile.close()
    ofile.close()
print('completed successfully')
