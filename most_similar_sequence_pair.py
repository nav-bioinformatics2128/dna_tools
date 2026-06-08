from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

best_similarity = 0

best_pair = ""

for i in range(0, len(records), 2):

    seq1 = records[i].seq
    seq2 = records[i + 1].seq

    differences = 0

    for j in range(len(seq1)):

        if seq1[j] != seq2[j]:

            differences += 1

    similarity = ((len(seq1) - differences) / len(seq1)) * 100

    if similarity > best_similarity:

        best_similarity = similarity

        best_pair = records[i].id + " vs " + records[i + 1].id

print("Most Similar Pair:")

print(best_pair)

print("Similarity:", round(best_similarity, 2), "%")
