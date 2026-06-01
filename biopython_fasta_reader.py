from Bio import SeqIO

for record in SeqIO.parse("sample.fasta", "fasta"):

    print("ID:", record.id)

    print("Sequence:", record.seq)

    print("Length:", len(record.seq))

    print()
