from Bio import SeqIO

motif = "ATG"

records = list(SeqIO.parse("sample.fasta", "fasta"))

high_density_count = 0

for record in records:

    sequence = str(record.seq)

    motif_count = sequence.count(motif)

    density = motif_count / len(sequence)

    if density > 0.05:

        high_density_count += 1

percentage = (high_density_count / len(records)) * 100

print("High Density Sequences:")

print(high_density_count)

print("Percentage:")

print(round(percentage, 2), "%")
