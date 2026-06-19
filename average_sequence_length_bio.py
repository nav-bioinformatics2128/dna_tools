from Bio import SeqIO

total_length = 0
count = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    total_length += len(record.seq)

    count += 1

average_length = total_length / count

print("Average Length:", round(average_length, 2))
