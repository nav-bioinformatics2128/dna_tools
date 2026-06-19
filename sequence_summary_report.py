from Bio import SeqIO

longest_length = 0
longest_id = ""

shortest_length = float("inf")
shortest_id = ""

total_length = 0
count = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    seq_length = len(record.seq)

    total_length += seq_length

    count += 1

    if seq_length > longest_length:

        longest_length = seq_length
        longest_id = record.id

    if seq_length < shortest_length:

        shortest_length = seq_length
        shortest_id = record.id

average_length = total_length / count

print("Total Sequences:", count)

print("Longest Sequence:", longest_id)
print("Longest Length:", longest_length)

print("Shortest Sequence:", shortest_id)
print("Shortest Length:", shortest_length)

print("Average Length:",
      round(average_length, 2))
