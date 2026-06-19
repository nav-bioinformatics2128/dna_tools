from Bio import SeqIO

highest_gc = 0

highest_gc_id = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    g_count = sequence.count("G")

    c_count = sequence.count("C")

    gc_percent = ((g_count + c_count)
                  / len(sequence)) * 100

    if gc_percent > highest_gc:

        highest_gc = gc_percent

        highest_gc_id = record.id

print("Highest GC Sequence:")

print(highest_gc_id)

print("GC%:", round(highest_gc, 2))
