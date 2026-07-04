from Bio import SeqIO

total_gc = 0
count = 0

highest_gc = 0
highest_id = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    gc_count = sequence.count("G") + sequence.count("C")

    gc_percent = (gc_count / len(sequence)) * 100

    print(record.id,
          round(gc_percent, 2))

    total_gc += gc_percent

    count += 1

    if gc_percent > highest_gc:

        highest_gc = gc_percent

        highest_id = record.id

average_gc = total_gc / count

print()

print("Average GC:",
      round(average_gc, 2))

print("Highest GC Sequence:",
      highest_id)

print("Highest GC:",
      round(highest_gc, 2))
