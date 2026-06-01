from Bio import SeqIO

shortest_seq = None
shortest_id = ""

for record in SeqIO.parse("sample.fasta", "fasta"):

    if shortest_seq is None:

        shortest_seq = record.seq
        shortest_id = record.id

    elif len(record.seq) < len(shortest_seq):

        shortest_seq = record.seq
        shortest_id = record.id

print("Shortest ID:", shortest_id)

print("Shortest Sequence:", shortest_seq)

print("Length:", len(shortest_seq))
