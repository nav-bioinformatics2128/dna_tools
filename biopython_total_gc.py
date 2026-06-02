from Bio import SeqIO

total_gc = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    gc = record.seq.count("G") + record.seq.count("C")

    total_gc += gc

print("Total GC Bases:", total_gc)
