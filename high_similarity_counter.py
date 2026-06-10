from Bio import SeqIO

records = list(SeqIO.parse("sample.fasta", "fasta"))

high_similarity_count = 0

for i in range(0, len(records), 2):

    seq1 = records[i].seq
    seq2 = records[i + 1].seq

    differences = 0

    for j in range(len(seq1)):

        if seq1[j] != seq2[j]:

            differences += 1

    similarity = ((len(seq1) - differences) / len(seq1)) * 100

    if similarity > 90:

        high_similarity_count += 1

print("Pairs Above 90% Similarity:")

print(high_similarity_count)
