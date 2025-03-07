'''
 takes 2 inputs:
    1. parties: a 2D list of parties (and the amount of pizza eaten by each individual within a party)
        - similar to the input taken in part 4B
    2. total_cost: a list of the total cost for each party (from the 2D list 'parties')

AFTER CALCULATING DISCOUNTED PRICE BASED ON THE DAY: 
should return a list of dictionaries:
    - dictionary key: a day of the week (Sunday, Wednesday, or Friday)
    - dictionary value: a 2D list (each inner list corresponds to the parties list. 
        the dict. value lists should be the amount an individual pays based on the amount of pizza they ate)
'''

def problem4c(parties: list, total_cost: list) -> list:
    #Code your function here
    input = [parties, total_cost] #Simply to see Input/Output return. You should use parties and total_cost in your function, not input.

    
    output = False # Please set your answer to this
    #return output structure: Output: [{'Sunday': [[]]}, {'Wednesday': [[]]}, {'Friday': [[]]}]
    return {"Input": input, "Output": output} # DO NOT MODIFY THIS LINE


if __name__ == '__main__':
    #Test your code here

    print(problem4c([[1/2, 1/8, 3/4, 5/8], [1/2, 1, 1/8]], [11, 13])) 
    #result: 
    # Input: [[[1/2, 1/8, 3/4, 5/8], [1/2, 1, 1/8]], [11, 13]]

    # Output:[
    # {'Sunday': [[2.06, 0.52, 3.09, 2.58], [3.0, 6.0, 0.75]]},
    # {'Wednesday': [[2.34, 0.58, 3.51, 2.92], [3.4, 6.8, 0.85]]}, 
    # {'Friday': [[2.2, 0.55, 3.3, 2.75], [3.2, 6.4, 0.8]]} ]
        
    
