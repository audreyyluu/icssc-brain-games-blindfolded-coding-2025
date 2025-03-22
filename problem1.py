import io
import contextlib

def problem1():
    """
    This function prints the necessarys statements for problem 1.
    
    Args:
        None
    
    Returns:
        output: fetched from STDIN (so be sure to only use print statements for your answers)
    """
    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
        # DO NOT MODIFY ABOVE THIS LINE

        # Code your print statements here

        # DO NOT MODIFY BELOW THIS LINE
        output = buf.getvalue().splitlines()

    return {"Input": None, "Output": output}  # DO NOT MODIFY THIS LINE

if __name__ == '__main__':
    # Feel free to add additional tests here
    print(problem1())