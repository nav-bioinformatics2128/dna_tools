from Bio import SeqIO

motif = "ATG"

highest_count = 0
best_sequence = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    count = sequence.count(motif)

    if count > highest_count:

        highest_count = count

        best_sequence = record.id

print("Sequence with Most Motifs:")

print(best_sequence)

print("Motif Count:")

print(highest_count)
