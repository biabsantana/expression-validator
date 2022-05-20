def valid_expression(string):
    pair_brackets = { 
        ')':'(',
        ']':'[',
        '}':'{'
    }
    stack = []
    for i in string:
        if i in pair_brackets.values():
            stack.append(i)
        elif i in pair_brackets.keys():
            if not stack:
                return False
            if stack[-1] == pair_brackets[i]: # peek the last stack item and check if it`s equal to the closed bracket founded
                stack.pop()
            else:
                return False
    return not stack