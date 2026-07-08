from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

total_length = 0

for record in records:

    total_length += len(record.seq)

average_length = total_length / len(records)

farthest_id = ""
largest_difference = 0

for record in records:

    difference = abs(len(record.seq) - average_length)

    if difference > largest_difference:

        largest_difference = difference

        farthest_id = record.id

print("Average Length:")

print(round(average_length, 2))

print()

print("Farthest Sequence:")

print(farthest_id)

print("Difference:")

print(round(largest_difference, 2))
