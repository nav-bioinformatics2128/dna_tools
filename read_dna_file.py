file = open("dna_sequences.txt", "r")

for line in file:

    print(line.strip())

file.close()
