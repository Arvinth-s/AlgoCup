
# JUDGEMENT DAY 2

  

[Practice]([https://www.codechef.com/SALC2021/problems/ALGOCUP6](https://www.codechef.com/SALC2021/problems/ALGOCUP6))

[Div-2 Contest]([https://www.codechef.com/SALC2021](https://www.codechef.com/SALC2021))

  
  

*Author:* [Arvinth Saravanan]([https://www.codechef.com/users/arvinth_sari](https://www.codechef.com/users/arvinth_sari))

*Tester:* [Tester's name]([https://www.codechef.com/users/tester_nick](https://www.codechef.com/users/tester_nick))

  

# DIFFICULTY:

HARD.

  
  

# PREREQUISITES:

DP, basics of graph

  

# PROBLEM:

Given a graph G and values of each node, val[i], find a path such that it maximizes the product of number of nodes in the path and the minimum of values those nodes. You can visit a node only once and the nodes are connected to at max two other nodes.

  

# QUICK EXPLANATION:

The graph can be converted to array of arrays and the problem is equivalent to finding the largest rectangle area in a histogram

  

# EXPLANATION:


The problem can be broken down into four parts  
1. Interpretation as graphs  
2. Conversion to an array of arrays data structure  
3. Identification of the problem  
4. Solving the dynamic programming problem.

### PART 1 - INTERPRETATION (EASY)  
- The interpretation of the problem statement as a graph problem is straightforward.  
- Each island is considered as a node, and each path between the islands is considered  as edges.  
- Since it’s a two-way path, the graph is undirected

### PART 2 - CONVERSION (MODERATE)  
- The graph is either linear or circuilar since an island is connected to at max two other islands.
-  As shown in the illustration a general graph can contain many connected components.  
- A linear graph component can be represented with an array.  
- A node can't be revisited hence cyclic paths are not allowed. So a cyclic component can also effectively represented as an array by slicing at any arbitrary edge. Thus, each connected components can be represented as an array
- Hence, the graph can be represented using an array of array say G. Since there's no path between the connected components traversal is allowed only within an array

### PART 3: IDENTIFICATION (MODERATE)  
- A path can be uniquely identified by the index of the connected component in G, say G[i], and starting and ending node in that connected component, G[i][start] and G[i][end]. 
- The sum of the virtue level of the group is equal to the product of the number of  
islands visited and the minimum virtue level of the islands visited 
 ```(end - start +1) * min(G[i][start], G[i][start+1], ..., G[i][end])```  
- The above equation is equivalent to the solution of finding largest rectangle area in a histogram

### PART 4: SOLVING DP (MODERATE)  
- Solving the Largest Rectangular Area in a Histogram problem

  

For adding mathematical expressions, LaTeX is required, which is nicely explained at [https://en.wikibooks.org/wiki/LaTeX/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics)

  

Some examples of latex here. (Latex is always enclosed in between $ sign)

  

$ans = \sum_{i = 1}^{N} a_i^k \bmod M$

  

$\frac{num}{den}$

  

$\leq$, $\geq$, $\neq$, $\pm$

  

# ALTERNATE EXPLANATION:

Could contain more or less short descriptions of possible other approaches.

  

# SOLUTIONS:

  

[details="Setter's Solution"]

indent whole code by 4 spaces

[/details]

  

[details="Tester's Solution"]

indent whole code by 4 spaces

[/details]

  

[details="Editorialist's Solution"]

indent whole code by 4 spaces

[/details]