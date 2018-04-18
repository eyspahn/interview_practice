# Given a list of people with their birth and death years, find the year with the highest population.

## Thinking about it on my own

## What does input list like?

### Most obvious/brute force way to do this: keep a tally of the years people are alive. Create an array, one slot for each year, then iterate through people and add a count for all the years each person has been alive.


# From Video
1. Listen
    Check Assumptions (e.g. people won't be alive at same time.)
    Data structure coming in?
2. Example
    Is example generic/big enough to capture the problem?
    Covers enough cases?
    Make data out of order, include duplicates if need be
3. Brute Force Algorithm (don't code yet)
    Check all years and count people alive in each year.
    What will the RUNTIME be?
        Check min birth year    O(p) , where p is # people
        Check max death year    O(p)
        Create array             
        Go through all years, add up people  O(p*Y), where y is # years
        Get max value   
        --> O(p*Y)
    Ask if interviewer wants to code up.
4. Optimize
    Really, only need to check years where someone was born or died.
    Edge case/ambiguity - what to return when multiple years.
    Only need to check unique years, not every year listed.
        Hash table/hash set - have I already calculated this year
    Now:
        Walk through each person, for each person
            How many people were alive in birth year
            How many people were alive in death year
        O(p^2)

    Refinement:
        Walk through each person, for each person
            Only checking unique years in each birth/death years
        O(Unique_years * Num_people) = O(U*P)

    Refinement:
        Looking for highest population.
            Will occur in birth years.
            Deaths do not increase population -> not a max year!
        So now:
            Walk through all people
            Check only birth years, how many people are alive that year.

    Refinement:
        Try to represent the data in a different way!
        On a number line.
        Note: It doesn't matter who dies when, it just decrements the population.
        Revised algo: just keep track of the count of people alive given birth/death years --> linear time.
            Put everything on a number line from earlierst bith to last death.
            Birth : += 1
            Death : -+ 1
            Walk through and find the highest algo

    Don't code until you know exactly what you need to do. Walk through algo again.
    Don't code if you don't know what your data structures are.

        Find min birth year     O(P)
        Find max death year --> no, use max birth year!     O(P)
        Create an array initialized to 0, will hold all values  O(Years)
        Have a table which will keep track of increment/decrement value.
            BUT: got clarification: that death year means they're alive that entire year. So the decrement happens the year after!
        Then walk through the table and keep count of population (running sum)  O(P)
        Get the running sum     O(Y)
        Pick the max population from that list.

        Total runtime: O(P+Y)

5. Walk through
6. Implement
    She uses Java
