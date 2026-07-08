from Bio import SeqIO

motif = "ATG"

highest_gc = 0
best_id = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    if motif in sequence:

        gc_count = sequence.count("G") + sequence.count("C")

        gc_percent = (gc_count / len(sequence)) * 100

        if gc_percent > highest_gc:

            highest_gc = gc_percent

            best_id = record.id

print("Highest GC Sequence Containing Motif:")

print(best_id)

print("GC Content:")

print(round(highest_gc, 2))
