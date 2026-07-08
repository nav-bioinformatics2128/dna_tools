from Bio import SeqIO

lower_limit = 40
upper_limit = 60

count = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    gc_count = sequence.count("G") + sequence.count("C")

    gc_percent = (gc_count / len(sequence)) * 100

    if lower_limit <= gc_percent <= upper_limit:

        count += 1

        print(record.id)

        print("GC:", round(gc_percent, 2))

        print()

print("Sequences in GC Range:")

print(count)
