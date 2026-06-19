from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

total_length = 0

for record in records:

    total_length += len(record.seq)

average_length = total_length / len(records)

above_average = 0

for record in records:

    if len(record.seq) > average_length:

        above_average += 1

print("Average Length:",
      round(average_length, 2))

print("Sequences Above Average:",
      above_average)
