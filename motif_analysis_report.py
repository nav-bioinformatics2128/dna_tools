from Bio import SeqIO

motif = "ATG"

total_motifs = 0
sequence_count = 0

highest_count = 0
highest_id = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    count = sequence.count(motif)

    total_motifs += count

    sequence_count += 1

    if count > highest_count:

        highest_count = count

        highest_id = record.id

average = total_motifs / sequence_count

print("=== Motif Analysis Report ===")

print("Motif:", motif)

print("Total Sequences:", sequence_count)

print("Total Motif Occurrences:", total_motifs)

print("Average Motifs Per Sequence:",
      round(average, 2))

print("Most Motif-Rich Sequence:",
      highest_id)

print("Highest Motif Count:",
      highest_count)
