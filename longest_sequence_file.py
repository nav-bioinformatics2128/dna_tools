file = open("dna_sequences.txt", "r")

longest_sequence = ""

for line in file:

    dna = line.strip()

    if len(dna) > len(longest_sequence):

        longest_sequence = dna

file.close()

print("Longest Sequence:")
print(longest_sequence)

print("Length:", len(longest_sequence))
