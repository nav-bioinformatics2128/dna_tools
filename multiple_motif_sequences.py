from Bio import SeqIO

motif = "ATG"

count_sequences = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence = str(record.seq)

    motif_count = sequence.count(motif)

    if motif_count > 1:

        count_sequences += 1

        print(record.id,
              motif_count)

print()

print("Sequences with More Than One Motif:")

print(count_sequences)
