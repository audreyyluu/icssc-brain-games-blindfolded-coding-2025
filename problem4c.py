def problem4c(parties: list, total_cost: list) -> list:
    input = [parties, total_cost] #IGNORE/DO NOT MODIFY. SIMPLY FOR RETURN FUNCTIONALITY.

    """
    This function calculates the cost of pizza for each person in each party.
    
    Args: 
        parties (nested list): Each inner list represents a party with 
                             each value inside representing the amount
                             of pizza that individual ate.

        total_cost (list): A list of the total costs for each party based on the pizza they ate
                            **Assume party discount from problem4b has already been calculated**
                            
    Returns: 
        output: A list of dictionaries representing the the cost for every person in each party.
                The key is the discounted day of the week and the value is a nested list (each inner
                list representing a party) with the calculated individual costs. 
    """
    
    #Code your function here
    
    output = False # Please set your answer to this
 
    return {"Input": input, "Output": output} # DO NOT MODIFY THIS LINE


if __name__ == '__main__':
    #Test your code here

    print(problem4c([[1/2, 1/8, 3/4, 5/8], [1/2, 1, 1/8]], [11, 13])) 
    # Output:[
    # {'Sunday': [[2.06, 0.52, 3.09, 2.58], [3.0, 6.0, 0.75]]},
    # {'Wednesday': [[2.34, 0.58, 3.51, 2.92], [3.4, 6.8, 0.85]]}, 
    # {'Friday': [[2.2, 0.55, 3.3, 2.75], [3.2, 6.4, 0.8]]} ]
        
