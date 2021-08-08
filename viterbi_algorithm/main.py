import viterbi as vit
import numpy as np


def main(args):
    path = args.path
    scale_both = args.scale_both
    scale_log = args.scale_log
    scale_norm = args.scale_norm
    reverse = args.reverse

    # Load sequence and sample data
    content = vit.read_lines_from_textfile(path)

    dice_number_sequence = content[0].split()[1]

    if len(content) > 1:
        hidden_state_sequence_actual = content[1].split()[1]
        hidden_state_viterbi_sample = content[2].split()[1]

    # State transition probabilities
    M = np.array(
        [[0.95, 0.05], [0.05, 0.95]]  # Fair dice to F and L
    )  # Loaded dice  to F and L

    # Initial state probabilites
    initial_prob = np.array([0.5, 0.5])

    # Emission probabilities
    E = np.array(
        [
            [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6],  # Fair dice
            [1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 2],  # Loaded dice
        ]
    )

    if reverse:
        print("Original Sequence: ", dice_number_sequence)
        dice_number_sequence = dice_number_sequence[::-1]
        print("Reversed Sequence: ", dice_number_sequence)

    observation_sequence = vit.convert_to_viterbi_input(
        dice_number_sequence)

    if scale_both:
        # Run Viterbi algorithm without log scale
        optimal_state_sequence, accumulated_probability, backtracking = vit.viterbi(
            transition_matrix=M,
            initial_state_matrix=initial_prob,
            emission_matrix=E,
            observations=observation_sequence,
        )
        print("- - - - Optimaler Pfad - Normal - - - -")
        print(vit.map_state_path(optimal_state_sequence))

        # Run Viterbi algorithm with log scale
        (
            log_optimal_state_sequence,
            log_accumulated_probability,
            log_backtracking,
        ) = vit.viterbi_logarithm(
            transition_matrix=M,
            initial_state_matrix=initial_prob,
            emission_matrix=E,
            observations=observation_sequence,
        )
        print("- - - - Optimaler Pfad - Logarithmiert - - - -")
        print(vit.map_state_path(log_optimal_state_sequence))
    if scale_norm and not scale_both:
        # Run Viterbi algorithm without log scale
        optimal_state_sequence, accumulated_probability, backtracking = vit.viterbi(
            transition_matrix=M,
            initial_state_matrix=initial_prob,
            emission_matrix=E,
            observations=observation_sequence,
        )
        print("- - - - Optimaler Pfad - Normal - - - -")
        print(vit.map_state_path(optimal_state_sequence))

    if scale_log and not scale_both:
        # Run Viterbi algorithm with log scale
        (
            log_optimal_state_sequence,
            log_accumulated_probability,
            log_backtracking,
        ) = vit.viterbi_logarithm(
            transition_matrix=M,
            initial_state_matrix=initial_prob,
            emission_matrix=E,
            observations=observation_sequence,
        )
        print("- - - - Optimaler Pfad - Logarithmiert - - - -")
        print(vit.map_state_path(log_optimal_state_sequence))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Calculate viterbi path from a given file')

    parser.add_argument('path', type=str,
                        default="wuerfel2020.txt",
                        help='The path of the file containing just a dice number sequence')

    parser.add_argument('--scale_both', action='store_true', default=False,
                        help='Print path with logarithmic and normal scale.')

    parser.add_argument('--scale_log', action='store_true', default=False,
                        help='Print path with logarithmic scale.')

    parser.add_argument('--scale_norm', action='store_true', default=True,
                        help='Print path with normal scale.')

    parser.add_argument('--reverse', action='store_true', default=False,
                        help='Reverses the input the sequence.')

    args = parser.parse_args()

    main(args)
