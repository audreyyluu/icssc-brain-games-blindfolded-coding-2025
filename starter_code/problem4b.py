def problem4b(input):
    """
    This function calculates the cost of pizza for each party.
    
    Args: 
        input (nested list): Each inner list represents a party with 
                             each value inside representing the amount
                             of pizza that individual ate.
    Returns: 
        list: A list of integers representing the cost per party.
    """
    # Code your function here

    output = False # Please set your answer to this
    return {"Input": input, "Output": output} # DO NOT MODIFY THIS LINE



if __name__ == "__main__":
    # Feel free to add additional tests here
    sample_input = [[1/2, 3/8, 1/4, 1/8], [3/8, 3/8, 5/8, 1/2, 1/8, 5/8, 1/2]]
    print(problem4b(sample_input)) # Output should be [25, 67]