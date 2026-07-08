from Bio import SeqIO

motif = "ATG"

total_gc = 0
count = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    if motif in sequence:

        gc_count = sequence.count("G") + sequence.count("C")

        gc_percent = (gc_count / len(sequence)) * 100

        total_gc += gc_percent

        count += 1

average_gc = total_gc / count

print("Average GC of Sequences Containing Motif:")

print(round(average_gc, 2))
