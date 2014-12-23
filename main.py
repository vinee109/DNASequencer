import sys
import sequencer
"""
Retrieves input from a file and returns the generated sequence
"""

def get_input():
    """
    Reads in the input from stdin and returns it as a list of lines
    """
    reads = sys.stdin.read().splitlines()
    return reads

if __name__ == '__main__':
	reads = get_input()
	print sequencer(reads)
