from Bio import SeqIO

total_length = 0
sequence_count = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    total_length += len(record.seq)

    sequence_count += 1

average_length = total_length / sequence_count

print("Total Sequences:", sequence_count)

print("Average Length:", round(average_length, 2))
