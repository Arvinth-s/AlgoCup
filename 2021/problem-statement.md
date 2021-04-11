OM NAMO NARAYANA

**AlgoCup**
**Judgement Day**

Description: Karma is a boomerang.



Problem statement: You died last night and it's your judgement day. Your sins and virtues are being weighed. It turns out that both weighs exactly same. Your given a task which is your last opportunity to reach the doors of heaven. <br/>

You will be reborn as a saint in a planet far from earth. The planet consists of n islands. Your job is to civilize the islands (not mandatorily all). Each island has it's virtue level and you will get a follower from each island you visit. <br/>

At each island the virtue level of you and your followers will drop down to the minimum of your current virtue level and virtue level of that island. You and your followers will go to heaven if the sum of the final virtue level of all members in the group (including you) is greater than k. Find whether you will go to hell or heaven.<br/>

Assume initally you have infinite virtue level and it's mandatory to visit atleast one island. You can start at any island and stop at any island and you will visit all the islands along the path. You can't visit an island twice.


Input format: 
- The first line will contain number of islands n and number of paths m
- The next n line will contain v[i], the virtue level of each island.
- The next m lines contains two integers u[i] and v[i] which describes a bi-directional path between the islands
- Next line contains k, the minimum net virtue of your group to reach heaven

Output format:
If the net virtue of your group is less than k, print "Hell". Otherwise print "Heaven".

