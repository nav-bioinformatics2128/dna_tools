from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

highest_similarity = -1
lowest_similarity = 101

best_pair = ""
worst_pair = ""

for i in range(0, len(records), 2):

    seq1 = records[i].seq
    seq2 = records[i + 1].seq

    differences = 0

    for j in range(len(seq1)):

        if seq1[j] != seq2[j]:

            differences += 1

    similarity = ((len(seq1) - differences) / len(seq1)) * 100

    pair_name = records[i].id + " vs " + records[i + 1].id

    if similarity > highest_similarity:

        highest_similarity = similarity
        best_pair = pair_name

    if similarity < lowest_similarity:

        lowest_similarity = similarity
        worst_pair = pair_name

print("Most Similar Pair:")
print(best_pair)
print("Similarity:", round(highest_similarity, 2), "%")

print()

print("Least Similar Pair:")
print(worst_pair)
print("Similarity:", round(lowest_similarity, 2), "%")
