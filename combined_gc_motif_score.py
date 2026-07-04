from Bio import SeqIO

motif = "ATG"

best_score = 0
best_id = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    motif_count = sequence.count(motif)

    motif_density = motif_count / len(sequence)

    gc_count = sequence.count("G") + sequence.count("C")

    gc_percent = (gc_count / len(sequence)) * 100

    score = motif_density + (gc_percent / 100)

    if score > best_score:

        best_score = score

        best_id = record.id

print("Best Sequence:")

print(best_id)

print("Score:")

print(round(best_score, 4))
