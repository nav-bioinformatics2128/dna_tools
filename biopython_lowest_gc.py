from Bio import SeqIO

lowest_gc = None
lowest_gc_id = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    gc = record.seq.count("G") + record.seq.count("C")

    gc_percent = (gc / len(record.seq)) * 100

    if lowest_gc is None:

        lowest_gc = gc_percent
        lowest_gc_id = record.id

    elif gc_percent < lowest_gc:

        lowest_gc = gc_percent
        lowest_gc_id = record.id

print("Lowest GC Sequence:")

print(lowest_gc_id)

print("GC %:", round(lowest_gc, 2))
