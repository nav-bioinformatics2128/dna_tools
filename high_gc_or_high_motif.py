from Bio import SeqIO

motif = "ATG"

selected_count = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    gc_count = sequence.count("G") + sequence.count("C")

    gc_percent = (gc_count / len(sequence)) * 100

    motif_count = sequence.count(motif)

    if gc_percent > 50 or motif_count > 1:

        selected_count += 1

        print(record.id)

        print("GC:",
              round(gc_percent, 2))

        print("Motifs:",
              motif_count)

        print()

print("Selected Sequences:")

print(selected_count)
