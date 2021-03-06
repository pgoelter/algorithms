import numpy as np


def viterbi(transition_matrix, initial_state_matrix, emission_matrix, observations):
    """Viterbi algorithm

    Args:
        transition_matrix (np.ndarray): State transition probability matrix of dimension I x I
        initial_state_matrix (np.ndarray): Initial state distribution  of dimension I
        emission_matrix (np.ndarray): Emission probability matrix of dimension I x K
        observations (np.ndarray): Observation sequence of length N

    Returns:
        opt_state_sequence (np.ndarray): Optimal state sequence of length N
        acc_probability_matrix (np.ndarray): Accumulated probability matrix
        backtracking_matrix (np.ndarray): Backtracking matrix
    """
    n_states = transition_matrix.shape[0]  # Number of states
    N = len(observations)  # Length of observation sequence

    # Initialize accumulated probability and backtracking matrices
    acc_probability_matrix = np.zeros((n_states, N))

    state = np.zeros((n_states, N)).astype(np.int32)

    forward_matrix = np.zeros((n_states, N))
    backward_matrix = np.zeros((n_states, N))

    acc_probability_matrix[:, 0] = np.multiply(
        initial_state_matrix, emission_matrix[:, observations[0]]
    )
    forward_matrix[0, 0] = initial_state_matrix[0] * emission_matrix[0, observations[0]]
    forward_matrix[1, 0] = initial_state_matrix[1] * emission_matrix[1, observations[0]]

    # Calculate accumulated probability and backtracking
    for n in range(1, N):
        for i in range(n_states):
            temp_product = np.multiply(
                transition_matrix[:, i], acc_probability_matrix[:, n - 1]
            )

            acc_probability_matrix[i, n] = (
                    np.max(temp_product) * emission_matrix[i, observations[n]]
            )

            state[i, n - 1] = np.argmax(temp_product)

            tmp_forward = np.multiply(
                transition_matrix[:, i], forward_matrix[:, n - 1]
            )

            forward_matrix[i, n] = (
                    np.sum(tmp_forward) * emission_matrix[i, observations[n]]
            )

    # Backtracking
    opt_state_sequence = np.zeros(N).astype(np.int32)
    opt_state_sequence[-1] = np.argmax(acc_probability_matrix[:, -1])
    backward_matrix[:, -1] = 1
    for n in range(N - 2, -1, -1):
        for i in range(n_states):
            tmp_backward = np.multiply(transition_matrix[:, i], backward_matrix[:, n + 1])

            backward_matrix[i, n] = np.sum(tmp_backward * emission_matrix[i, observations[n + 1]])

        opt_state_sequence[n] = state[int(
            opt_state_sequence[n + 1]), n]

    return opt_state_sequence, acc_probability_matrix, state


def viterbi_logarithm(transition_matrix, initial_state_matrix, emission_matrix, observations):
    """Viterbi algorithm (log variant)

    Args:
        transition_matrix (np.ndarray): State transition probability matrix of dimension I x I
        initial_state_matrix (np.ndarray): Initial state distribution  of dimension I
        emission_matrix (np.ndarray): Output probability matrix of dimension I x K
        observations (np.ndarray): Observation sequence of length N

    Returns:
        opt_state_sequence (np.ndarray): Optimal state sequence of length N
        acc_probability_log (np.ndarray): Accumulated log probability matrix
        backtracking_matrix (np.ndarray): Backtracking matrix
    """
    n_states = transition_matrix.shape[0]  # Number of states
    N = len(observations)  # Length of observation sequence

    transition_log = np.log(transition_matrix)

    initial_log = np.log(initial_state_matrix)

    emission_log = np.log(emission_matrix)

    # Initialize accumulated probability and backtracking matrices
    acc_probability_log = np.zeros((n_states, N))

    state = np.zeros((n_states, N)).astype(np.int32)

    acc_probability_log[:, 0] = initial_log + emission_log[:, observations[0]]

    # Calculate accumulated probability and backtracking
    for n in range(1, N):
        for i in range(n_states):
            temp_sum = transition_log[:, i] + acc_probability_log[:, n - 1]

            acc_probability_log[i, n] = (
                    np.max(temp_sum) + emission_log[i, observations[n]]
            )

            state[i, n - 1] = np.argmax(temp_sum)

    # Backtracking
    opt_state_sequence = np.zeros(N).astype(np.int32)
    opt_state_sequence[-1] = np.argmax(acc_probability_log[:, -1])
    for n in range(N - 2, -1, -1):
        opt_state_sequence[n] = state[int(
            opt_state_sequence[n + 1]), n]

    return opt_state_sequence, acc_probability_log, state


def posteriori(transition_matrix, initial_state_matrix, emission_matrix, observations):
    """Posteriori decoding

    Args:
        transition_matrix (np.ndarray): State transition probability matrix of dimension I x I
        initial_state_matrix (np.ndarray): Initial state distribution  of dimension I
        emission_matrix (np.ndarray): Output probability matrix of dimension I x K
        observations (np.ndarray): Observation sequence of length N
    """
    n_states = transition_matrix.shape[0]  # Number of states
    N = len(observations)  # Length of observation sequence

    forward_matrix = np.zeros((n_states, N))
    backward_matrix = np.zeros((n_states, N))

    forward_matrix[0, 0] = initial_state_matrix[0] * emission_matrix[0, observations[0]]
    forward_matrix[1, 0] = initial_state_matrix[1] * emission_matrix[1, observations[0]]

    # Calculate accumulated probability and backtracking
    for n in range(1, N):
        for i in range(n_states):
            tmp = np.multiply(
                transition_matrix[:, i], forward_matrix[:, n - 1]
            )

            forward_matrix[i, n] = (
                    np.sum(tmp) * emission_matrix[i, observations[n]]
            )

    # Backtracking
    backward_matrix[:, -1] = 1

    for n in range(N - 2, -1, -1):
        for i in range(n_states):
            tmp_backward = np.multiply(transition_matrix[:, i], backward_matrix[:, n + 1])

            backward_matrix[i, n] = np.sum(tmp_backward * emission_matrix[i, observations[n + 1]])
    # TODO: Calculate total probability calculation and backtracing part.

    return NotImplemented
