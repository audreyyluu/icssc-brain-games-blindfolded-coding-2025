def problem4c(parties: list, total_cost: list) -> list:
    input = [parties, total_cost] #IGNORE/DO NOT MODIFY. SIMPLY FOR RETURN FUNCTIONALITY.
    
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
        
