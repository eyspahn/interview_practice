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
