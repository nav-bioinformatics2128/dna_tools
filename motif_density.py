from Bio import SeqIO

motif = "ATG"

highest_density = 0
best_sequence = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    motif_count = sequence.count(motif)

    density = motif_count / len(sequence)

    if density > highest_density:

        highest_density = density

        best_sequence = record.id

print("Highest Motif Density Sequence:")

print(best_sequence)

print("Density:")

print(round(highest_density, 4))
