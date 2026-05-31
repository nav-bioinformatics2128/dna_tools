file = open("dna_sequences.txt", "r")

shortest_sequence = None

for line in file:

    dna = line.strip()

    if shortest_sequence is None:

        shortest_sequence = dna

    elif len(dna) < len(shortest_sequence):

        shortest_sequence = dna

file.close()

print("Shortest Sequence:")
print(shortest_sequence)

print("Length:", len(shortest_sequence))
