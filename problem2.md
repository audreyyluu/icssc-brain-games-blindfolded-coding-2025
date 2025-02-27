# Problem 2: The Traveling Pizza Courier Problem

You step out of the kitchen, pizza boxes balanced in your arms like a precarious stack of unsubmitted assignments.

The pizzas need to get to their tables—but you have no idea where those tables are.

You check your pockets. Empty. You retrace your steps. No luck. You briefly consider asking someone for help, but then you remember that one guy last week who started his answer with "Well, technically…" and you knew you were doomed.

Fine. No map, no problem. You’re at (0,0), and if you can figure out where the tables are, you can take the shortest route and get this over with.

Find the best route—or take the scenic (and shameful) one.

## The Task
Write a function that determines the most efficient delivery route given a list of three table coordinates. Assume you start at (0,0), and return a list of coordinates in the order they should be visited to minimize total travel distance.
- Input will be a list of three tuples
- *Hint: Find the distance to the closest table and then the 2 possible paths and print the shortest one*
<br></br>

    **Sample Input**:
    `[(1,7), (3,4), (2,5)]`

    **Sample Output**:
    `[(3,4), (2,5), (1,7)]`
