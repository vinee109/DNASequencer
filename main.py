import sys

def get_input():
    """
    Reads in the input from stdin and returns it as a list of lines
    """
    reads = sys.stdin.read().splitlines()
    return reads
