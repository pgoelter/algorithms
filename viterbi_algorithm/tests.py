import viterbi as vit
import pytest
import numpy as np

@pytest.fixture
def dice_sequence():
    return "31236546661"

@pytest.fixture
def emission_probabilities():
    E = np.array(
        [
            [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6],  # Fair dice
            [1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 2],  # Loaded dice
        ]
    )
    return E


@pytest.fixture
def transition_probabilities():
    # State transition probabilities
    M = np.array(
        [[0.95, 0.05],  # Fair dice to F and L
         [0.05, 0.95]]  # Loaded dice  to F and L
    )
    return M


@pytest.fixture
def initial_state_probabilities():
    initial_prob = np.array([0.5, 0.5])
    return initial_prob


def test_viterbi_vs_viterbi_logarithm(initial_state_probabilities, transition_probabilities, emission_probabilities, dice_sequence):
    observations = vit.convert_to_viterbi_input(dice_sequence)
    optimal_state_sequence, _, _ = vit.viterbi(
        transition_matrix=transition_probabilities,
        initial_state_matrix=initial_state_probabilities,
        emission_matrix=emission_probabilities,
        observations=observations,
    )
    opt_seq_string = vit.map_state_path(optimal_state_sequence)

    optimal_state_sequence, _, _ = vit.viterbi_logarithm(
        transition_matrix=transition_probabilities,
        initial_state_matrix=initial_state_probabilities,
        emission_matrix=emission_probabilities,
        observations=observations,
    )
    opt_seq_string_log = vit.map_state_path(optimal_state_sequence)

    assert opt_seq_string == opt_seq_string_log, "Log and normal scale sequence is not the same"


def test_viterbi_reversed_vs_viterbi(initial_state_probabilities, transition_probabilities, emission_probabilities, dice_sequence):

    observations = vit.convert_to_viterbi_input(dice_sequence)
    observations_reversed = vit.convert_to_viterbi_input(dice_sequence[::-1])

    optimal_state_sequence, _, _ = vit.viterbi(
        transition_matrix=transition_probabilities,
        initial_state_matrix=initial_state_probabilities,
        emission_matrix=emission_probabilities,
        observations=observations,
    )
    opt_seq_string = vit.map_state_path(optimal_state_sequence)
    optimal_state_sequence_rev, _, _ = vit.viterbi(
        transition_matrix=transition_probabilities,
        initial_state_matrix=initial_state_probabilities,
        emission_matrix=emission_probabilities,
        observations=observations_reversed,
    )
    opt_seq_string_reversed = vit.map_state_path(optimal_state_sequence_rev)

    #assert opt_seq_string == opt_seq_string_reversed[::-1]

    optimal_state_sequence_log, _, _ = vit.viterbi_logarithm(
        transition_matrix=transition_probabilities,
        initial_state_matrix=initial_state_probabilities,
        emission_matrix=emission_probabilities,
        observations=observations,
    )
    opt_seq_string_log = vit.map_state_path(optimal_state_sequence)

    optimal_state_sequence_log_rev, _, _ = vit.viterbi_logarithm(
        transition_matrix=transition_probabilities,
        initial_state_matrix=initial_state_probabilities,
        emission_matrix=emission_probabilities,
        observations=observations_reversed,
    )
    opt_seq_string_log_rev = vit.map_state_path(optimal_state_sequence)
    #assert opt_seq_string_log == opt_seq_string_log_rev[::-1]
