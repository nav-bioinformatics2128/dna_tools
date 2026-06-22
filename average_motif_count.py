from Bio import SeqIO

motif = "ATG"

total_count = 0
sequence_count = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    count = sequence.count(motif)

    total_count += count

    sequence_count += 1

average = total_count / sequence_count

print("Average Motif Count:")

print(round(average, 2))
