from Bio import SeqIO

motif = "ATG"

all_positions = []

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    for i in range(len(sequence) - len(motif) + 1):

        if sequence[i:i+len(motif)] == motif:

            all_positions.append(i)

print("Total Motif Positions:")

print(len(all_positions))

print("Positions:")

print(all_positions)
