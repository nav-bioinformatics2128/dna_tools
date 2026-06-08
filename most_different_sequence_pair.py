from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

max_differences = 0

best_pair = ""

for i in range(0, len(records), 2):

    seq1 = records[i].seq
    seq2 = records[i + 1].seq

    differences = 0

    for j in range(len(seq1)):

        if seq1[j] != seq2[j]:

            differences += 1

    if differences > max_differences:

        max_differences = differences

        best_pair = records[i].id + " vs " + records[i + 1].id

print("Most Different Pair:")
print(best_pair)

print("Differences:", max_differences)
