import viterbi as vit
import numpy as np


def main():
    # Load sequence and sample data
    content = vit.read_lines_from_textfile("wuerfel2021.txt")

    dice_number_sequence = content[0].split()[1]
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
            [1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 2],
        ]
    )  # Loaded dice

    observation_sequence = vit.convert_to_viterbi_input(dice_number_sequence)  # [::-1])

    # Run Viterbi algorithm without log scale
    optimal_state_sequence, accumulated_probability, backtracking = vit.viterbi(
        transition_matrix=M,
        initial_state_matrix=initial_prob,
        emission_matrix=E,
        observations=observation_sequence,
    )
    # print(vit.map_state_path(optimal_state_sequence))

    # Run Viterbi algorithm with log scale

    (
        log_optimal_state_sequence,
        log_accumulated_probability,
        log_backtracking,
    ) = vit.viterbi_log(
        transition_matrix=M,
        initial_state_matrix=initial_prob,
        emission_matrix=E,
        observations=observation_sequence,
    )

    # print(vit.map_state_path(optimal_state_sequence))


if __name__ == "__main__":
    main()
