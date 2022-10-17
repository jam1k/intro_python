
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    

    elif (my_string[0] != '(' and my_string[0] != ')' and my_string[0] != '[' and my_string[0] != ']'):
        return balanced_brackets(my_string[1:])
    
    elif (my_string[-1] != '(' and my_string[-1] != ')' and my_string[-1] != '[' and my_string[-1] != ']'):
        return balanced_brackets (my_string[:-1])
    
    elif (my_string[0] != '(' or my_string[-1] != ')') and (my_string[0] != '[' or my_string[-1] != ']'):
        return False
    elif (my_string.count("(") != my_string.count(")")) or (my_string.count("[") != my_string.count("]")):
        return False
    
    
    # remove first and last character
    return balanced_brackets(my_string[1:-1])

if __name__ == "__main__":

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)
