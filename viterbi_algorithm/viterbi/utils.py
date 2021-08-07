from typing import List
import numpy as np

STATE_MAP = {0: "F", 1: "L"}


def convert_string(s: str) -> List[int]:
    """Convert a string containing only numbers to a list of integers."""
    return [int(c) for c in s]


def reverse_list(l: List[int]) -> List[int]:
    """Reverse a list."""
    return list(reversed(l))


def read_lines_from_textfile(filename: str) -> List[str]:
    """Reads lines from a text file."""
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def convert_to_viterbi_input(s: str) -> List[int]:
    """Convert a string to a list of integers. This only works in the context of sequences of dice numbers. We substract 1 as the indexing start with 0 not 1."""
    return np.array(convert_string(s)) - 1


def map_state_path(path: List[int]) -> List[int]:
    """Map the state path to a string."""
    return "".join([STATE_MAP[s] for s in path])


def info(optimal_sequence, acc_prob, backtracking):
    """Print information about result of the viterbi algorithm."""
    print("Optimal state sequence: S = ", map_state_path(optimal_sequence))
    # print("Accumulated Prob. Matrix =", acc_prob, sep="\n")
    # print("Backtracking Matrix =", backtracking, sep="\n")
