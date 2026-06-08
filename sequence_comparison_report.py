from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

report = open("comparison_report.txt", "w")

for i in range(0, len(records), 2):

    seq1 = records[i].seq
    seq2 = records[i + 1].seq

    differences = 0

    for j in range(len(seq1)):

        if seq1[j] != seq2[j]:

            differences += 1

    report.write(records[i].id + " vs " +
                 records[i + 1].id + "\n")

    report.write("Differences: " +
                 str(differences) + "\n\n")

report.close()

print("Report Created")
