from Bio import SeqIO

longest_seq = ""
longest_id = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    if len(record.seq) > len(longest_seq):

        longest_seq = record.seq

        longest_id = record.id

print("Longest Sequence ID:", longest_id)

print("Length:", len(longest_seq))
