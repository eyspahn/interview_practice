#
# From Goodrich's Data Structures & Algorithms sec 6.1.4
# The section on stacks.
# Write a function to check if delimeters "({[" match
# Returns true/false, true if balanced
# Help from http://www.ardendertat.com/2011/11/08/programming-interview-questions-14-check-balanced-parentheses/


def is_matched(expr):
    lefts = '([{'
    rights = ')]}'
    stack = []
    if len(expr)==0:
        return False
    else:
        for ch in expr:
            if ch in lefts:
                stack.append(ch)
            else:
                if not stack:
                    return False
                last_open = stack.pop()
                if rights.index(ch)!=lefts.index(last_open):
                    return False
    return len(stack)==0
