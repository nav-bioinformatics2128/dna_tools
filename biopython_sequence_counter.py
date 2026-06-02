from Bio import SeqIO

count = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    count += 1

print("Total Sequences:", count)
