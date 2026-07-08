from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

total_length = 0
total_gc = 0

longest = 0
shortest = float("inf")

for record in records:

    sequence = str(record.seq)

    length = len(sequence)

    gc_count = sequence.count("G") + sequence.count("C")

    gc_percent = (gc_count / length) * 100

    total_length += length

    total_gc += gc_percent

    if length > longest:

        longest = length

    if length < shortest:

        shortest = length

average_length = total_length / len(records)

average_gc = total_gc / len(records)

print("===== DATASET SUMMARY =====")

print("Total Sequences:", len(records))

print("Average Length:", round(average_length, 2))

print("Average GC:", round(average_gc, 2))

print("Longest Sequence:", longest)

print("Shortest Sequence:", shortest)
