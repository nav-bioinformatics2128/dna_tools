from Bio import SeqIO

count = 0
total_length = 0

for record in SeqIO.parse("sample.fasta", "fasta"):

    count += 1

    total_length += len(record.seq)

average_length = total_length / count

report = open("summary_report.txt", "w")

report.write("FASTA SUMMARY\n")

report.write("Total Sequences: " + str(count) + "\n")

report.write("Average Length: " + str(round(average_length, 2)) + "\n")

report.close()

print("Report saved.")
