from Bio import SeqIO

count = 0
total_length = 0
total_gc = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    count += 1

    total_length += len(record.seq)

    total_gc += record.seq.count("G") + record.seq.count("C")

average_length = total_length / count

report = open("fasta_report.txt", "w")

report.write("FASTA REPORT\n\n")

report.write("Total Sequences: " + str(count) + "\n")

report.write("Total Length: " + str(total_length) + "\n")

report.write("Average Length: " + str(round(average_length, 2)) + "\n")

report.write("Total GC Bases: " + str(total_gc) + "\n")

report.close()

print("Report Created")
