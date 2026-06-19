from Bio import SeqIO

longest_length = 0
longest_id = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    sequence_length = len(record.seq)

    if sequence_length > longest_length:

        longest_length = sequence_length

        longest_id = record.id

print("Longest Sequence:", longest_id)

print("Length:", longest_length)
