from Bio import SeqIO

motif = "ATG"

total_count = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    count = sequence.count(motif)

    total_count += count

print("Total motif occurrences:")

print(total_count)
