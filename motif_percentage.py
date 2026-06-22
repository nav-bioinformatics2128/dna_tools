from Bio import SeqIO

motif = "ATG"

records = list(SeqIO.parse("sample.fasta", "fasta"))

motif_count = 0

for record in records:

    sequence = str(record.seq)

    if motif in sequence:

        motif_count += 1

percentage = (motif_count / len(records)) * 100

print("Sequences Containing Motif:")

print(motif_count)

print("Percentage:")

print(round(percentage, 2), "%")
