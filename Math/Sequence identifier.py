def find_changes(sequence):                            # Finds changes between values in a list
    changes = []
    for i in range(len(sequence)-1):
        changes.append(sequence[i+1]-sequence[i])
    return changes

def identify_sequence(changes):                            # Identifies the sequence
    level = 0
    while True:
        changes = find_changes(changes)
        level += 1
        print("Level ",level,": ",changes)
        
        if len(changes) < 2:
            return "Insufficient values"
        
        done = True
        for i in range(len(changes)-1):
            if changes[i] != changes[i+1]:
                done = False
        
        if done:
            break

while True:                                                       # Inputs sequence length
    try:
        sequence_length = int(input("How many values?: "))
        if sequence_length > 0:
            break
        else:
            print("Sequence length has to be more than 0.")
    except ValueError:
        print("Invalid value entered, has to be int.")

sequence = []

while len(sequence) < sequence_length:                            # Inputs the sequence
    try:
        sequence.append(int(input("Enter a value: ")))
    except ValueError:
        print("Invalid value entered, has to be int.")

identify_sequence(sequence)
