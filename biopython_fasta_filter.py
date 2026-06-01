from Bio import SeqIO

output_file = open("filtered.fasta", "w")

for record in SeqIO.parse("sample.fasta", "fasta"):

    if len(record.seq) > 5:

        SeqIO.write(record, output_file, "fasta")

output_file.close()

print("Filtered sequences saved.")
