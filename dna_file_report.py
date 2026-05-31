file = open("dna_sequences.txt", "r")

count = 0
total_bases = 0

longest_sequence = ""
shortest_sequence = None

for line in file:

    dna = line.strip()

    count += 1

    total_bases += len(dna)

    if len(dna) > len(longest_sequence):

        longest_sequence = dna

    if shortest_sequence is None:

        shortest_sequence = dna

    elif len(dna) < len(shortest_sequence):

        shortest_sequence = dna

file.close()

average_length = total_bases / count

print("DNA FILE REPORT")

print("=" * 30)

print("Total Sequences :", count)

print("Total Bases :", total_bases)

print("Average Length :", round(average_length, 2))

print("Longest Sequence :", longest_sequence)

print("Shortest Sequence :", shortest_sequence)
