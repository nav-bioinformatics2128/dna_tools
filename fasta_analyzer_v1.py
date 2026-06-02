from Bio import SeqIO

count = 0
total_length = 0

longest_seq = ""
shortest_seq = None

for record in SeqIO.parse("sample.fasta", "fasta"):

    count += 1

    total_length += len(record.seq)

    if len(record.seq) > len(longest_seq):

        longest_seq = record.seq

    if shortest_seq is None:

        shortest_seq = record.seq

    elif len(record.seq) < len(shortest_seq):

        shortest_seq = record.seq

average_length = total_length / count

print("FASTA ANALYZER")

print("Total Sequences:", count)

print("Average Length:", round(average_length, 2))

print("Longest Length:", len(longest_seq))

print("Shortest Length:", len(shortest_seq))
