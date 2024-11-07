def detect_sequence(transitions):
    states = {}
    initial_state = None
    final_state = None
    sequence = ""

    # Parse transitions and store in a dictionary
    for present_state, next_state, input_val, output in transitions:
        if present_state not in states:
            states[present_state] = {}
        states[present_state][input_val] = (next_state, output)
        if initial_state is None:
            initial_state = present_state
        if output == '1':
            final_state = next_state

    # Detect the sequence by traversing the state transitions
    current_state = initial_state
    sequence_detected = False
    while not sequence_detected:
        for input_val, (next_state, output) in states[current_state].items():
            sequence += input_val
            current_state = next_state
            if output == '1':  # Sequence is detected when we see output '1'
                sequence_detected = True
                break

    # Determine if the sequence detector is overlapping or non-overlapping
    if final_state and states.get(final_state, {}).get('1', ('', '0'))[1] == '1' and final_state == current_state:
        detector_type = "Non Overlapping Sequence Detector"
    else:
        detector_type = "Overlapping Sequence Detector"

    return sequence, detector_type


# Input processing
def main():
    transitions = []
    print("Enter each transition line in the format: <present_state> <next_state> <input> <output>")
    print("Press Enter on an empty line to finish i nput.")

    while True:
        line = input().strip()
        if not line:  # Stop reading if an empty line is entered
            break
        transitions.append(line.split())

    sequence, detector_type = detect_sequence(transitions)
    print(sequence)
    print(detector_type)


if __name__ == "__main__":
    main()

