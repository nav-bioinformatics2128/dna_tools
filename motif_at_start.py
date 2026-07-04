from Bio import SeqIO

motif = "ATG"

count = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    if sequence.startswith(motif):

        count += 1

        print(record.id)

print()

print("Sequences Starting with Motif:")

print(count)
