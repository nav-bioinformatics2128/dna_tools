from Bio import SeqIO

motif = "ATG"

records = list(SeqIO.parse("sample.fasta", "fasta"))

total_count = 0

for record in records:

    sequence = str(record.seq)

    total_count += sequence.count(motif)

average = total_count / len(records)

print("Average Motif Count:",
      round(average, 2))

print()

print("Sequences Above Average:")

for record in records:

    sequence = str(record.seq)

    count = sequence.count(motif)

    if count > average:

        print(record.id,
              count)
