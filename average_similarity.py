from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

total_similarity = 0

pair_count = 0

for i in range(0, len(records), 2):

    seq1 = records[i].seq
    seq2 = records[i + 1].seq

    differences = 0

    for j in range(len(seq1)):

        if seq1[j] != seq2[j]:

            differences += 1

    similarity = ((len(seq1) - differences) / len(seq1)) * 100

    total_similarity += similarity

    pair_count += 1

average_similarity = total_similarity / pair_count

print("Average Similarity:", round(average_similarity, 2))
