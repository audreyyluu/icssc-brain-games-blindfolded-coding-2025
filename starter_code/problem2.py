import math

def problem2(locations : list[tuple]):
    """
    This function calculates the most efficient delivery route 
    for three tables' coordinates.
    
    Args:
        locations (list[tuples]): A list of three tuples, each tuple is the
                      Cartesian coordinates (x and y) of a table.
    
    Returns:
        output (list[tuples]): The reordered list from input with the 
                               tuples in the order to be traversed.
    """
    # Code your function here


    
    output = [] # Please set your answer to this
    return {"Input": locations, "Output": output} # DO NOT MODIFY THIS LINE

if __name__ == '__main__':
    sample_input = [(1,7), (3,4), (2,5)]
    print(problem2(sample_input)) # should be [(3,4), (2,5), (1,7)]
