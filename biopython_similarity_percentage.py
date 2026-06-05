from Bio.Seq import Seq

seq1 = Seq("ATGCGA")
seq2 = Seq("ATGCCA")

matches = 0

for i in range(len(seq1)):

    if seq1[i] == seq2[i]:

        matches += 1

similarity = (matches / len(seq1)) * 100

print("Similarity %:", round(similarity, 2))
