file = open("sample.fasta", "r")

sequences = {}

header = ""

for line in file:

    line = line.strip()

    if line.startswith(">"):

        header = line

    else:

        sequences[header] = line

file.close()

print(sequences)
