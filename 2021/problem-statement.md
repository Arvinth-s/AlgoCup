OM NAMO NARAYANA

**AlgoCup**
**Judgement Day**

# Description:
A dp approach 



# Problem statement: 
You are going to be born as a saint in a planet far from earth. The planet consists of n islands. Your job is to civilize the islands (not mandatorily all). Each island has it's virtue level and you will get a follower from each island you visit. <br/>

At each island the virtue level of you and your followers will drop down to the minimum of your current virtue level and virtue level of that island. You and your followers will go to heaven if the sum of the final virtue level of all members in the group (**excluding you**) is greater than k. Find maximum value of k for which your group can go to heaven.<br/>

Assume initally you have infinite virtue level and it's mandatory to visit atleast one island. You can start at any island and stop at any island and you will visit all the islands along the path. You can't visit an island more than once.




# Input format: 
- The first line will contain number of islands n and number of paths m
- The next line will contain n spaced integers val[i], the virtue level of each island.
- The next m lines contains two integers u[i] and v[i] which describes a bi-directional path between the islands


# Constraints
- Each island is connected to at max 2 islands
- n <= 10<sup>5</sup>
- 0 <= v[i] <= 10<sup>4</sup>

# Output format:
print the maximum value of k

