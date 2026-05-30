file = open("dna_sequences.txt", "r")

total_bases = 0

for line in file:

    dna = line.strip()

    total_bases += len(dna)

file.close()

print("Total Bases :", total_bases)
